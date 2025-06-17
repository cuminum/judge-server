from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'autovim'
    command = 'autovim'
    test_program = """\
normal iecho: Hello, World!
"""