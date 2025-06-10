from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'arcyou'
    command = 'arcyou'
    test_program = """\
"echo: Hello, World!"
"""
    nproc = -1
    syscalls = ['execve', 'wait4', 'chdir']