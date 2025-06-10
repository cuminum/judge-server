from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'abc'
    command = 'abc'
    test_program = """\
WRITE "echo: Hello, World!"
"""
    nproc = -1
    syscalls = ['execve']