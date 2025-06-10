from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'apl'
    command = 'apl'
    test_program = """\
⎕←'echo: Hello World!'
"""