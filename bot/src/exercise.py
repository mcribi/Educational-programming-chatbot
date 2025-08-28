# Class of Exercise 
# atributes: type, question, options, answer, explanation, tests_json, hint, solution_code, checker, float_tol, time_limit_ms, memory_limit_mb
class Exercise:
    def __init__(
        self,
        type_,
        question,
        options=None,
        answer="",
        explanation=None,
        *,
        tests_json=None,
        hint=None,
        solution_code=None,
        checker="normalized",
        float_tol=None,
        time_limit_ms=1500,
        memory_limit_mb=128,
    ):
        self.type = type_
        self.question = question
        self.options = options
        self.answer = answer
        self.explanation = explanation

        #optional atributes
        self.tests_json = tests_json or {}
        self.hint = hint
        self.solution_code = solution_code
        self.checker = checker
        self.float_tol = float_tol
        self.time_limit_ms = time_limit_ms
        self.memory_limit_mb = memory_limit_mb

    def is_correct(self, user_answer: str) -> bool:
        """
        For test exercises clasical comparate and for code exercises depends on the runner with the test
        """
        if self.type == "code":
            return False  # the validation is made by the runner (/run, /submit)
        return user_answer.strip().lower() == (self.answer or "").strip().lower()
