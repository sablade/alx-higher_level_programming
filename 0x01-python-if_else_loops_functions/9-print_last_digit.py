#!/usr/bin/python3
def print_last_digit(number):
    lst = abs(number) % 10
    if number < 0:
        lst = lst * -1
    print("{:d}".format(lst), end="")
