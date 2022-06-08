#!/usr/bin/env python3

import os, sys


# ------------------------------------------------
#
# main
#
# ------------------------------------------------
def main():
    i = 0

    where = "In main"
    
    p_dict = {}
    p_dict['i'] = i

    i += 10
    
    fee(p_dict)
    
    sys.exit(0)
    # End of main


# ------------------------------------------------
#
# fee
#
# ------------------------------------------------
def fee(p_dict):
    j = 0

    where = "In fee"
    
    p_dict['i'] += 1
    p_dict['j'] = j

    j += 20
    
    fie(p_dict)
    
    return
    # End of fee

    
# ------------------------------------------------
#
# fie
#
# ------------------------------------------------
def fie(p_dict):
    k = 0

    where = "In fie"
    
    p_dict['i'] += 1
    p_dict['j'] += 1
    p_dict['k'] = k

    k += 30

    foo(p_dict)
    
    return
    # End of fie

    
# ------------------------------------------------
#
# foo
#
# ------------------------------------------------
def foo(p_dict):
    l = 0

    where = "In foo"
    
    p_dict['i'] += 1
    p_dict['j'] += 1
    p_dict['k'] += 1
    p_dict['l'] = l

    l += 40
    fum(p_dict)
    
    return
    # End of foo

    
# ------------------------------------------------
#
# fum
#
# ------------------------------------------------
def fum(p_dict):
    m = 0

    where = "In fum"
    
    p_dict['i'] += 1
    p_dict['j'] += 1
    p_dict['k'] += 1
    p_dict['l'] += 1
    p_dict['m'] = m

    m += 50
    
    return
    # End of fum

    
# ------------------------------------------------
#
# Entry point
#
# ------------------------------------------------
if __name__ == '__main__':
    main()
    
