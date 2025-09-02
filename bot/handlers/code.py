# bot/handlers/code.py
# -----------------------------------------------------------------------------
# Handlers for the "Programar (C++)" mode:
# - Capture student's code messages (markdown ```cpp ... ``` or raw C++).
# - /run: run only sample tests (quick feedback).
# - /submit: run sample + hidden tests (final verdict). Accept if all pass
#            or (optionally) if code matches solution_code exactly.
# - /solution: show official solution (marks attempt as SOLUTION).
# - /hint: show single hint if available.
#
# Attempts are saved using a best-effort approach that adapts to your Attempt
# model (fields are set only if they exist).
# -----------------------------------------------------------------------------

import re
from typing import Optional, List, Tuple

from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import CommandHandler, MessageHandler, filters

from db.database import get_session
from db.models.exercise import Exercise as ExerciseModel
from db.models.topic import Topic  # potentially useful if you route by topic
from db.models.user import User
from utils.runner_client import run_tests
from utils.runner_client import run_cpp, RunnerError
from telegram import InlineKeyboardMarkup, InlineKeyboardButton



# Try to import Attempt model; if not present, we'll no-op on save_attempt
try:
    from db.models.attempt import Attempt
except Exception:
    Attempt = None  # type: ignore

# -----------------------------------------------------------------------------
# Keys and simple policy
# -----------------------------------------------------------------------------
CODE_KEY = "last_code"              # stores last code sent by user
EX_KEY = "current_exercise_id"      # must be set when user selects an exercise

MAX_CODE_CHARS = 4000
FORBIDDEN_PATTERNS = [
    r'\bsystem\s*\(',
    r'\bfork\s*\(',
    r'\bexec[lvp]\w*\s*\(',
    r'#\s*include\s*<filesystem>',
    r'#\s*include\s*<thread>',
    r'#\s*include\s*<future>',
    r'#\s*include\s*<chrono>',
    r'#\s*include\s*<regex>',
]

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def is_code_block(text: str) -> bool:
    """Accept markdown ```...``` or plain code starting with #include or containing 'int main'."""
    if not text:
        return False
    t = text.strip()
    if t.startswith("```"):
        return True
    head = t[:80].lower()
    return head.startswith("#include") or "int main" in head

def extract_code(text: str) -> Optional[str]:
    """Extract code from ```cpp ... ``` or return raw text if it looks like C++."""
    if not text:
        return None
    m = re.search(r"```(?:cpp|c\+\+|cc)?\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    t = text.strip()
    return t if is_code_block(t) else None

def violates_simple_policy(code: str) -> Optional[str]:
    """Basic length and banned includes/funcs check."""
    if len(code) > MAX_CODE_CHARS:
        return f"El código es demasiado largo ({len(code)} caracteres). Máximo permitido: {MAX_CODE_CHARS}."
    for pat in FORBIDDEN_PATTERNS:
        if re.search(pat, code):
            return "Tu código usa funciones/bibliotecas no permitidas en este entorno por seguridad."
    return None

def get_exercise_and_tests(context: ContextTypes.DEFAULT_TYPE) -> Tuple[Optional[ExerciseModel], List[dict], List[dict]]:
    """Load current exercise from DB and split tests_json into sample/hidden lists of dicts."""
    ex_id = context.user_data.get(EX_KEY)
    if not ex_id:
        return None, [], []
    with get_session() as s:
        ex = s.get(ExerciseModel, ex_id)
        if not ex or ex.type != "code":
            return None, [], []
        tj = ex.tests_json or {}
        sample = tj.get("sample", []) or []
        hidden = tj.get("hidden", []) or []
        # Normalize to simple dicts {input, output}
        sample = [{"input": t.get("input", ""), "output": t.get("output", "")} for t in sample]
        hidden = [{"input": t.get("input", ""), "output": t.get("output", "")} for t in hidden]
        return ex, sample, hidden

def same_code(a: str, b: str) -> bool:
    """Exact code match ignoring trailing spaces per line."""
    def norm(s: str) -> str:
        return "\n".join(line.rstrip() for line in s.strip().splitlines())
    return norm(a) == norm(b)

def get_or_create_user_by_telegram(session, telegram_id: int, name: Optional[str]) -> User:
    """Return app user (DB) for a given telegram_id, creating it if needed."""
    u = session.query(User).filter(User.telegram_id == telegram_id).one_or_none()
    if u:
        return u
    u = User(telegram_id=telegram_id, name=name)
    session.add(u)
    session.commit()
    session.refresh(u)
    return u

def code_actions_keyboard() -> InlineKeyboardMarkup:
    """Inline keyboard shown after code results in code-mode."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("ℹ️ Ayuda", callback_data="code_help")],
        [
            InlineKeyboardButton("🔁 Siguiente enunciado", callback_data="repeat_mode"),
            InlineKeyboardButton("⬅ Volver al menú de práctica", callback_data="back_to_mode"),
        ],
    ])


def save_attempt(
    *,
    telegram_id: int,
    exercise_id: int,
    code: str,
    status: str,         # 'AC', 'WA', 'CE', 'RE', 'TLE', 'SOLUTION'
    passed: int = 0,
    total: int = 0,
    is_correct: Optional[bool] = None,
    compile_log: Optional[str] = None,
    run_log: Optional[str] = None,
) -> None:
    """Best-effort Attempt persister that adapts to your Attempt model fields."""
    if Attempt is None:
        return  # Attempt model not available; skip persist
    with get_session() as s:
        # map telegram user to app user if Attempt expects user_id
        user = get_or_create_user_by_telegram(s, telegram_id, None)
        a = Attempt()  # type: ignore

        # Safely set fields only if they exist on the model
        if hasattr(a, "user_id"):
            setattr(a, "user_id", user.id)
        if hasattr(a, "telegram_id"):
            setattr(a, "telegram_id", telegram_id)
        if hasattr(a, "exercise_id"):
            setattr(a, "exercise_id", exercise_id)
        if hasattr(a, "code"):
            setattr(a, "code", code)
        if hasattr(a, "status"):
            setattr(a, "status", status)
        if hasattr(a, "passed"):
            setattr(a, "passed", passed)
        if hasattr(a, "total"):
            setattr(a, "total", total)
        if hasattr(a, "is_correct") and is_correct is not None:
            setattr(a, "is_correct", is_correct)
        if hasattr(a, "compile_log") and compile_log is not None:
            setattr(a, "compile_log", compile_log)
        if hasattr(a, "run_log") and run_log is not None:
            setattr(a, "run_log", run_log)

        s.add(a)
        s.commit()

# -----------------------------------------------------------------------------
# Entry points / UX
# -----------------------------------------------------------------------------
async def show_programming_intro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a short intro and wait for user's code."""
    context.user_data["awaiting_code"] = True
    text = (
        "💻 Modo *Programar* (C++)\n\n"
        "1) Elige un ejercicio de programación.\n"
        "2) Envía tu código *completo* (puedes usar bloque ```cpp ... ```).\n"
        "3) Usa /run para probar *ejemplos* y /submit para evaluar *todos los tests*.\n"
        "   Aceptado ⇢ si pasan todos los tests (o coincide con la solución oficial).\n\n"
        "Límites típicos: tiempo ~1.5s, memoria ~128MB. Algunas funciones/bibliotecas están restringidas.\n\n"
        "Ejemplo mínimo:\n"
        "```cpp\n"
        "#include <bits/stdc++.h>\n"
        "using namespace std;\n"
        "int main(){\n"
        "    cout << \"Hola\" << '\\n';\n"
        "}\n"
        "```\n"
        + code_help_text(short=True) #adding cheatsheet
    )
    if update.callback_query:
        await update.callback_query.message.edit_text(text, parse_mode="Markdown")
    else:
        await update.message.reply_text(text, parse_mode="Markdown")

# Capture any message that looks like code
async def handle_code_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Capture user code and store in user_data."""
    if not update.message or not update.message.text:
        return
    if not context.user_data.get("awaiting_code", False):
        # If you require an explicit mode toggle, keep this guard.
        # If not, you can remove it and always capture code-looking messages.
        pass

    code = extract_code(update.message.text)
    if not code:
        return  # ignore non-code messages silently

    policy_msg = violates_simple_policy(code)
    if policy_msg:
        await update.message.reply_text(f"⚠️ {policy_msg}")
        return

    context.user_data[CODE_KEY] = code
    await update.message.reply_text(
        "📝 Código recibido.\n\n"
        "• /out — compila y ejecuta *tu último código* y muestra **la salida tal cual**.\n"
        "• /run — ejecuta los *ejemplos* del ejercicio (feedback rápido).\n"
        "• /submit — ejecuta *todos* los tests y evalúa.\n"
        "• /hint — una pista (si hay).\n"
        "• /solution — solución oficial.",
        parse_mode="Markdown"
    )
    
# /run: run only sample tests
async def cmd_run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Run sample tests only (quick feedback)."""
    if CODE_KEY not in context.user_data:
        await update.message.reply_text("Primero envía tu solución en un bloque ```cpp ... ```.", parse_mode="Markdown")
        return

    ex, sample, _ = get_exercise_and_tests(context)
    if not ex:
        await update.message.reply_text("Selecciona primero un ejercicio de programación.")
        return
    if not sample:
        await update.message.reply_text("Este ejercicio no tiene casos de ejemplo configurados.")
        return

    code = context.user_data[CODE_KEY]
    res = await run_tests(
        code,
        sample,
        time_limit_ms=ex.time_limit_ms or 1500,
        memory_limit_mb=ex.memory_limit_mb or 128,
        checker=ex.checker or "normalized",
        float_tol=ex.float_tol
    )

    # Handle compilation error
    if res.get("status") == "CE":
        log = res.get("compile_log", "")
        await update.message.reply_text(f"❌ Error de compilación\n```\n{log}\n```", parse_mode="Markdown")
        # Save attempt (compile error)
        save_attempt(
            telegram_id=update.effective_user.id,
            exercise_id=ex.id,
            code=code,
            status="CE",
            passed=0,
            total=len(sample),
            is_correct=False,
            compile_log=log,
        )
        return

    passed, total = res.get("passed", 0), res.get("total", 0)
    msg = f"Ejecutado (ejemplos): {passed}/{total} OK."
    first_fail_detail = None
    for c in res.get("cases", []):
        if c["status"] != "AC":
            if c["status"] == "WA":
                first_fail_detail = f"\n❌ Caso {c['i']+1}: Wrong Answer\n{c.get('diff','')[:800]}"
            elif c["status"] == "RE":
                first_fail_detail = f"\n❌ Caso {c['i']+1}: Runtime Error\n```\n{c.get('stderr','')}\n```"
            elif c["status"] == "TLE":
                first_fail_detail = f"\n⏱️ Caso {c['i']+1}: Time Limit Exceeded"
            break
    if first_fail_detail:
        msg += first_fail_detail

    await update.message.reply_text(msg, parse_mode="Markdown")

    # Save attempt (sample run)
    save_attempt(
        telegram_id=update.effective_user.id,
        exercise_id=ex.id,
        code=code,
        status=res.get("status", "WA"),
        passed=passed,
        total=total,
        is_correct=False,
        run_log=first_fail_detail or "",
    )

# helper to get a valid reply target (works with messages and callbacks)
def _reply_target(update):
    if getattr(update, "message", None):
        return update.message
    if getattr(update, "callback_query", None) and update.callback_query.message:
        return update.callback_query.message
    return None

# /submit: run sample + hidden; accept on all pass or same_code with solution
async def cmd_submit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Run full test suite (sample + hidden)."""

    msg = _reply_target(update)

    if CODE_KEY not in context.user_data:
        text = "Primero envía tu solución en un bloque ```cpp ... ```."
        if msg:
            await msg.reply_text(text, parse_mode="Markdown")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode="Markdown")
        return

    ex, sample, hidden = get_exercise_and_tests(context)
    if not ex:
        text = "Selecciona primero un ejercicio de programación."
        if msg:
            await msg.reply_text(text)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        return

    tests = sample + hidden
    code = context.user_data[CODE_KEY]

    res = await run_tests(
        code,
        tests,
        time_limit_ms=ex.time_limit_ms or 1500,
        memory_limit_mb=ex.memory_limit_mb or 128,
        checker=ex.checker or "normalized",
        float_tol=ex.float_tol
    )

    # Compilation error
    if res.get("status") == "CE":
        log = res.get("compile_log", "")
        text = f"❌ Error de compilación\n```\n{log}\n```"
        if msg:
            await msg.reply_text(text, parse_mode="Markdown")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode="Markdown")
        save_attempt(
            telegram_id=update.effective_user.id,
            exercise_id=ex.id,
            code=code,
            status="CE",
            passed=0,
            total=len(tests),
            is_correct=False,
            compile_log=log,
        )
        return

    passed, total = res.get("passed", 0), res.get("total", 0)
    accepted = (passed == total) or (ex.solution_code and same_code(code, ex.solution_code))

    if accepted:
        text = f"✅ ¡Aceptado! Pasaste {passed}/{total} casos."
        if msg:
            await msg.reply_text(text)
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        save_attempt(
            telegram_id=update.effective_user.id,
            exercise_id=ex.id,
            code=code,
            status="AC",
            passed=total,
            total=total,
            is_correct=True,
        )
        return

    # Not accepted: report first failing case
    text = f"❌ No aceptado. Pasaste {passed}/{total}.\n"
    first_fail_detail = None
    for c in res.get("cases", []):
        if c["status"] != "AC":
            if c["status"] == "WA":
                first_fail_detail = f"Caso {c['i']+1}: Wrong Answer\n{c.get('diff','')[:800]}"
            elif c["status"] == "RE":
                first_fail_detail = f"Caso {c['i']+1}: Runtime Error\n```\n{c.get('stderr','')}\n```"
            elif c["status"] == "TLE":
                first_fail_detail = f"Caso {c['i']+1}: Time Limit Exceeded"
            break
    if first_fail_detail:
        text += first_fail_detail

    if msg:
        await msg.reply_text(text, parse_mode="Markdown")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode="Markdown")

    save_attempt(
        telegram_id=update.effective_user.id,
        exercise_id=ex.id,
        code=code,
        status=res.get("status", "WA"),
        passed=passed,
        total=total,
        is_correct=False,
        run_log=first_fail_detail or "",
    )


# /solution: show official solution (and save attempt as SOLUTION)
async def cmd_solution(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show official solution if available and mark attempt as SOLUTION."""
    if context.user_data.get("exam", {}).get("active"):
        await update.message.reply_text("⛔ Durante el examen no hay pistas ni solución.")
        return

    ex, _, _ = get_exercise_and_tests(context)
    if not ex or not ex.solution_code:
        await update.message.reply_text("No hay solución disponible para este ejercicio.")
        return

    await update.message.reply_text(f"Solución oficial:\n```cpp\n{ex.solution_code}\n```", parse_mode="Markdown")
    # Save a 'SOLUTION' attempt (not correct)
    code = context.user_data.get(CODE_KEY, "")
    save_attempt(
        telegram_id=update.effective_user.id,
        exercise_id=ex.id,
        code=code,
        status="SOLUTION",
        passed=0,
        total=0,
        is_correct=False,
    )

# /hint: send single hint if provided
async def cmd_hint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send single hint if the exercise has one."""
    if context.user_data.get("exam", {}).get("active"):
        await update.message.reply_text("⛔ Durante el examen no hay pistas ni solución.")
        return

    ex, _, _ = get_exercise_and_tests(context)
    if not ex or not ex.hint:
        await update.message.reply_text("No hay pista para este ejercicio.")
        return
    await update.message.reply_text(f"💡 Pista: {ex.hint}")

async def cmd_out(update, context):
    """Compile & run the last user code and print raw output (no tests)."""
    code = context.user_data.get(CODE_KEY)
    if not code:
        await update.message.reply_text(
            "Primero envíame tu código (puedes usar un bloque ```cpp ... ```).",
            parse_mode="Markdown"
        )
        return

    try:
        res = await run_cpp(code)
    except RunnerError as e:
        await update.message.reply_text(f"❌ Runner no disponible: {e}")
        return
    except Exception as e:
        await update.message.reply_text(f"❌ Error inesperado: {e}")
        return

    kb = code_actions_keyboard()

    if not res.get("ok"):
        # Show compiler/runtime error with actions
        stderr = (res.get("stderr") or "").strip() or "(sin detalle)"
        msg = (
            f"❌ Resultado de /out\n"
            f"```\n{stderr[:3500]}\n```\n"
            "Acciones rápidas: /run · /submit · /hint · /solution"
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=kb)
        return

    # OK: print raw stdout (+stderr if any), and show actions
    stdout = (res.get("stdout") or "").rstrip("\n")
    stderr = (res.get("stderr") or "").rstrip("\n")

    text = "✅ Resultado de /out\n"
    if stdout:
        text += f"```\n{stdout[:3500]}\n```"
    else:
        text += "_(sin salida por STDOUT)_"

    if stderr:
        text += f"\n\n_STDERR:_\n```\n{stderr[:1500]}\n```"

    text += "\n\nAcciones rápidas: /run · /submit · /hint · /solution"

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=kb)

# Cheatsheet for code mode commands (long and short variants)
def code_help_text(short: bool = False) -> str:
    if short:
        return (
            "ℹ️ *Comandos (Programar)*\n"
            "• /out — ejecuta tu último código y muestra la salida.\n"
            "• /run — ejecuta solo los ejemplos.\n"
            "• /submit — ejecuta todos los tests y evalúa.\n"
            "• /hint — una pista (si hay).\n"
            "• /solution — solución oficial."
        )
    # long version
    return (
        "🧭 *Comandos del modo Programar*\n"
        "• /out — Compila y ejecuta tu *último* código y muestra **la salida tal cual**.\n"
        "• /run — Ejecuta **solo** los *casos de ejemplo* del ejercicio (feedback rápido).\n"
        "• /submit — Ejecuta *todos* los tests (ejemplos + ocultos) y decide si está *Aceptado*.\n"
        "• /hint — Muestra *una sola* pista (si existe).\n"
        "• /solution — Muestra la solución oficial (marca el intento como *SOLUTION*).\n"
    )

async def cmd_code_help(update, context):
    """Show detailed help for code mode commands."""
    await update.message.reply_text(code_help_text(short=False), parse_mode="Markdown")



# -----------------------------------------------------------------------------
# Registration helper (optional if you register in main.py)
# -----------------------------------------------------------------------------
def register_handlers(app):
    """Convenience function to register these handlers in your Application."""
    app.add_handler(CommandHandler("run", cmd_run))
    app.add_handler(CommandHandler("submit", cmd_submit))
    app.add_handler(CommandHandler("solution", cmd_solution))
    app.add_handler(CommandHandler("hint", cmd_hint))
    app.add_handler(CommandHandler("out", cmd_out))
    app.add_handler(CommandHandler("codehelp", cmd_code_help))

    # Capture code-looking text (ensure this comes before generic text handlers)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_code_message))
