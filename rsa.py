#!/usr/bin/python3
import sys
import math
import random

def _isprime(num):
    """checks if a number is a prime number

    Args:
        num (int): positive input number

    Returns:
        True if number is prime else false
    """
    flag = True
    if num < 0 and (not isinstance(num, int)):
        return False

    if num in [2, 3, 5, 7, 11, 13, 17]:
        return True

    #tmp = list(range(19, num))
    #random.shuffle(tmp)
    for i in range(19, num):
        if (num % i) == 0:
            return False


def _fact(n):
    """Finds possible factors of a number
    Args:
        n (int): input natural number
    Returns:
        a list of two integers that multiplies to give input number
    """
    upper_bound = int(math.sqrt(n))
    for i in range(upper_bound, n):
        holder = [None, None]
        if n % i == 0 and _isprime(i):
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
