#!/usr/bin/python3
"""
Purpose: Relational Operations
    - These operations will result in a boolean value (True or False)

     <  lesser
     >  greater
     == equal to
     <= less than or equal to
     >= greater than or equal to
     != not equal to
     <> not equal to  ( in python 2 only)
"""
us_dollar = 74
canadian_dollar = 50

print("us_dollar = ", us_dollar)
print("canadian_dollar = ", canadian_dollar)
print()

print(f"us_dollar = {us_dollar}")
print(f"canadian_dollar = {canadian_dollar}")
print()

print(f"{us_dollar =}")
print(f"{canadian_dollar =}")
print()

print("us_dollar == canadian_dollar:", us_dollar == canadian_dollar)
print(f"{us_dollar == canadian_dollar = }")
print()

print(f"{us_dollar > canadian_dollar  = }")
print(f"{us_dollar >= canadian_dollar = }")
print(f"{us_dollar < canadian_dollar  = }")
print(f"{us_dollar <= canadian_dollar = }")
print(f"{us_dollar != canadian_dollar = }")
# print(f"{us_dollar <> canadian_dollar = }")  # works only in python 2.x

print()
print(f"{74 == 50 =}")
print(f"{74 != 50 =}")
print(f"{74 >  50 =}")
print(f"{74 >= 50 =}")
print(f"{74 <  50 =}")
print(f"{74 <= 50 =}")
print()


# == value-level equivalence check
# = assignment operator

74 == 74
# 74 = 74  SyntaxError: cannot assign to literal
a = 74
b = a
