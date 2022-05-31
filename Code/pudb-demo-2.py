#!/usr/bin/env python3

import os, sys

def main():

    i = 3

    for index in range(1, 20):
        j = index * i
        if j % 10 == 0:
            breakpoint()
        else:
            print(f"index value: {index}")
            

    sys.exit(0)
    # End of main

if __name__ == '__main__':
    main()
