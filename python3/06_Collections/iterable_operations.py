#!/usr/bin/python3
"""
Purpose: working with Iterables
"""
values = [1, 2, 3, 4, 2, 1, 3, 1, 4, 3, 3]
print(f"{values                        =}")
print()

print(f"{max(values)                   =}")
print(f"{values.count(2)               =}")
print(f"{values.count(3)               =}")
print(f"{max(values, key=values.count) =}")  # mode
print()

print(f"{min(values)                   =}")
print(f"{min(values, key=values.count) =}")
print()

# Method 1
add_result = 0
for num in values:
    add_result += num
print(f"{add_result                    =}")

# Method 2
print(f"{sum(values)                   =}")

print(f"{sum(values, start=0         ) =}")  # +0
print(f"{sum(values, start=4         ) =}")  # +4
print(f"{sum(values, start=100       ) =}")  # +100
print()


print(f"{sorted(values)                                  =}")
print(f"{sorted(values, key=values.count)                =}")
print(f"{sorted(values, key=values.count, reverse=True)  =}")
print(f"{sorted(values, key=values.count, reverse=False) =}")
print()

# list.reverse() and reversed() will reverse the order of assignment
values = [3, 2, 6, 4, 9, 5]
print(f"{values                 =}")
values.reverse()
print(f"{values                 =}")
print(f"{reversed(values)       =}")
print(f"{list(reversed(values)) =}")

# word = 'malayalam'
# print(f'{word                       = }')
# print(f'{max(word)                  = }')
# print(f'{min(word)                  = }')

# print(f'{max(word, key=values.count)  = }')
# print(f'{min(word, key=values.count)  = }')

# print(f'{max(list(word), key=values.count)  = }')
# print(f'{min(list(word), key=values.count)  = }')


values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"{values =}")

pairs = list(zip(values, values[1:]))
print(f"{pairs =}")

from itertools import islice

pairs = list(zip(values, islice(values, 1, None)))
print(f"{pairs =}")
