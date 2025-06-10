from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = '2sable'
    command = '2sable'
    test_program = """\
"echo: Hello, World!
"""
    syscalls = ['execve']