from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'bal'
    command = 'ballerina'
    test_program = """\
import ballerina/io;

// The `main` function, which acts as the entry point.
public function main() {
    io:println("Hello, World!");
}
"""