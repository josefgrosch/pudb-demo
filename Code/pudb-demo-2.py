#!/usr/bin/env python3

import sys
import time

def main():
    # export PYTHONBREAKPOINT="pudb.set_trace"
    a_dict = {}
    a_dict['this'] = 'that'

    foo()

    sys.exit(0)
    # End of main

def foo():

    bar()

    return
    # End of foo
    
def bar():
    i = 3

    for index in range(1, 20):
        j = index * i
        if j % 10 == 0:
            breakpoint()
        else:
            print(f"index value: {index}")
            time.sleep(1)
            
    return
    # End of bar
    
if __name__ == '__main__':
    main()
