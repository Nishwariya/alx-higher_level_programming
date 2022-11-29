#!/usr/bin/bash/python3
def print_last_digit(number):
    """prints the last digit of a number"""
    val = int(repr(number) [-1])
    print("{}".format(val), end="")
    return val
