from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'arithmetic'
    command = 'arithmetic'
    test_program = """\
2 = 2
10 = 10
10 = 5 + 5
6 = 6
6 - 5 = 1
20 = 40 / 2
20 + 0 = 2 + 18
20 = 2 * 10
1 / 0
"""
    nproc = -1
    syscalls = ['execve', 'wait4', 'fadvise64']