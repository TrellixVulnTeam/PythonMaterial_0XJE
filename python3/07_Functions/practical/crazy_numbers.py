#!python -u
"""
Purpose: Display the crazy numbers

Crazy number: A number whose digits are when raised to the power of the number of digits in that number and then added and if that sum is equal to the number then it is a crazy number.

Example:
Input: 123
Then, if 1^3 + 2^3 + 3^3 is equal to 123 then it is a crazy number.
"""


def crazy_num(num):
    total = 0
    while num:
        total += (num % 10) ** 3
        print(num, num // 10, num % 10, total)
        num = num // 10
        # breakpoint()
    print(total)
    # a = b = int(n)
    # c = 0  # 'c' is the var that stores the number of digits in 'n'.

    # s = 0  # 's' is the sum of the digits raised to the power of the num of digits.

    # while a != 0:
    #     a = int(a / 10)
    #     c += 1

    # while b != 0:
    #     rem = int(b % 10)
    #     s += rem ** c
    #     b = int(b / 10)

    # if s == n:
    #     print (f'{n:6} is Crazy number.')
    # # else:
    # #     print (f'{n:6} is Not crazy number.')


num = 10_00_000  # int(input("Enter number: "))

# for n in range(num):
#     crazy_num(n)
crazy_num(123)
