#!/usr/bin/python
"""
Purpose: Debugging with ipdb

TASK - To display all even numbers between 0 & 100

To install ipdb,
    pip install -U ipdb --user

"""
import ipdb

ipdb.set_trace()

numbers = range(0, 100)

for each_num in numbers:
    if each_num % 2 == 0:  # each_num % 2
        print(each_num, end=", ")

# Assignment: How to clear one specific breakpoint, in pdb
