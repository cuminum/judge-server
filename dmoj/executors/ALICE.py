from dmoj.executors.script_executor import ScriptExecutor

class Executor(ScriptExecutor):
    ext = 'alice'
    command = 'alice'
    test_program = """\
/
 "
  e
   c
    h
     o
      :
        
        H
         e
          l
           l
            o
             ,
               
               W
                o
                 r
                  l
                   d
                    !
                     "
                      O
                       @
"""
    syscalls = ['execve', 'eventfd2']