#!/usr/bin/python3
import sys

def _fact(n):
    """Finds possible factors of a number

    Args:
        n (int): input natural number

    Returns:
        a list of two integers that multiplies to give input number
    """
    holder = [None, None]
    for i in range(2, n):
        if n % i == 0:
            holder[0] = i
            holder[1] = int(n / i)
            return holder

with open(sys.argv[1], 'r') as file_buffer:
    for line in file_buffer:
        line = int(line)
        num = [None, None]
        if line != None:
            num = _fact(line)
            print(f"{line}={num[0]}*{num[1]}")
