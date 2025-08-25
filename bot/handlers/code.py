from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes
import re

from utils.runner_client import run_cpp, RunnerError

# basics limits
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

def is_code_block(text: str) -> bool:
    # accept: ```...``` or code plain thath begins with #include or int main(
    if text.strip().startswith("```"):
        return True
    head = text.strip()[:40].lower()
    return head.startswith("#include") or "int main" in head

def extract_code(text: str) -> str:
    """
    Si viene en bloque Markdown ```cpp ... ```, lo extraemos.
    Si viene sin ``` lo devolvemos tal cual.
    """
    m = re.search(r"```(?:cpp|c\+\+)?\s*(.*?)```", text, re.DOTALL|re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return text.strip()

def violates_simple_policy(code: str) -> str | None:
    if len(code) > MAX_CODE_CHARS:
        return f"El código es demasiado largo ({len(code)} caracteres). Máximo permitido: {MAX_CODE_CHARS}."
    for pat in FORBIDDEN_PATTERNS:
        if re.search(pat, code):
            return "Tu código usa funciones/bibliotecas no permitidas en este entorno por seguridad."
    return None

async def show_programming_intro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["awaiting_code"] = True
    context.user_data["stdin_expected"] = ""   
    text = (
        "💻 Modo *Programar* (C++)\n\n"
        "Pega tu código *completo* (lo puedes enviar tal cual o dentro de un bloque ```cpp ... ```).\n"
        "Límites: tiempo ~2s, memoria ~64MB. Funciones peligrosas/bibliotecas restringidas.\n\n"
        "Ejemplo mínimo:\n"
        "```cpp\n"
        "#include <bits/stdc++.h>\n"
        "using namespace std;\n"
        "int main(){\n"
        "    cout << \"Hola\" << endl;\n"
        "    return 0;\n"
        "}\n"
        "```\n"
        "¡Cuando quieras!"
    )
    if update.callback_query:
        await update.callback_query.message.edit_text(text, parse_mode="Markdown")
    else:
        await update.message.reply_text(text, parse_mode="Markdown")

async def receive_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # only if is waiting code
    if not context.user_data.get("awaiting_code"):
        return

    user_text = update.message.text or ""
    if not is_code_block(user_text):
        await update.message.reply_text(
            "Por favor, envía *solo código C++* (puedes usar ```cpp ... ```).",
            parse_mode="Markdown"
        )
        return

    code = extract_code(user_text)
    policy_msg = violates_simple_policy(code)
    if policy_msg:
        await update.message.reply_text(f"⚠️ {policy_msg}")
        return

    await update.message.reply_text("🔧 Compilando y ejecutando...", disable_web_page_preview=True)

    try:
        result = await run_cpp(code, stdin=context.user_data.get("stdin_expected",""))
    except RunnerError as e:
        await update.message.reply_text(f"❌ Error de conexión con el runner: {e}")
        return
    except Exception as e:
        await update.message.reply_text(f"❌ Error inesperado: {e}")
        return

    # format the result
    ok = result["ok"]
    stage = result["stage"]
    time_ms = result["time_ms"]
    exit_code = result["exit_code"]

    stdout = result["stdout"].strip()
    stderr = result["stderr"].strip()

    parts = []
    if ok:
        parts.append("✅ *Ejecución correcta*")
    else:
        if stage == "compile":
            parts.append("❌ *Error de compilación*")
        else:
            parts.append("❌ *Error en ejecución*")

    parts.append(f"⏱ {time_ms} ms")
    if exit_code is not None:
        parts.append(f"🔢 exit code: {exit_code}")

    header = " · ".join(parts)

    body = []
    if stdout:
        body.append(f"*STDOUT:*\n```\n{stdout[:1500]}\n```")
    if stderr:
        body.append(f"*STDERR:*\n```\n{stderr[:1500]}\n```")
    if not stdout and not stderr:
        body.append("_(sin salida)_")

    footer_kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔁 Probar otro", callback_data="repeat_mode"),
         InlineKeyboardButton("⬅ Elegir modo", callback_data="choose_mode")]
    ])

    await update.message.reply_text(
        f"{header}\n\n" + "\n\n".join(body),
        parse_mode="Markdown",
        reply_markup=footer_kb
    )
