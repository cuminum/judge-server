from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'arnoldc'
    command = 'arnoldc'
    test_program = """\
IT'S SHOWTIME
TALK TO THE HAND "echo: Hello, World!"
YOU HAVE BEEN TERMINATED
"""
    nproc = -1
    syscalls = ['execve']