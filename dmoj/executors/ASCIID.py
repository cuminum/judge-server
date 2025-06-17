from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'asciidots'
    command = 'asciidots'
    test_program = """\
.-$"echo: Hello, World!"
"""