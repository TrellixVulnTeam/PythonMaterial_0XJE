#!/usr/bin/python
"""
Purpose:
    break     - breaks the complete loop
	continue  - skip the current loop
	pass      - will do nothing. it is like a todo
	sys.exit  - will exit the script execution
"""


students = ["akram", "trusha", "bhavana", "jaya", "chaitra"]
print("break importance ==========")
for each_student in students:
    if each_student == "bhavana":
        break
    print(each_student)

print("continue importance ==========")
for each_student in students:
    if each_student == "bhavana":
        continue
    print(each_student)

print("pass importance ==========")
for each_student in students:
    if each_student == "bhavana":
        pass
    print(each_student)

import sys

print("sys.exit importance ==========")
for each_student in students:
    if each_student == "bhavana":
        sys.exit(0)
    print(each_student)

print("-------next statement")
