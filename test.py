#!/usr/bin/python3
import math
def _isprime(num):
    """checks if a number is a prime number

    Args:
        num (int): positive input number

    Returns:
        True if number is prime else false
    """
    if num < 0 and (not isinstance(num, int)):
        return False

    if num in [2, 3, 5]:
        return True

    if num < 2 or (num % 2) == 0 or (num % 3) == 0 or (num % 5) == 0:
        return False

    if (num %  7) == 0 or (num % 11) == 0 or (num % 13) == 0 or (num % 17) == 0 or (num % 19) == 0 or (num % 23) == 0 or (num % 29) == 0 or (num % 31) == 0 or (num % 37) == 0 or (num % 41) == 0 or (num % 43) == 0 or (num % 47) == 0 or (num % 53) == 0 or (num % 59) == 0:
        return False

    if num < 3481:
        return True
    
    for i in range(59, num):
        if (num % i) == 0:
            return False
    return True

def factorization(n):
    if n == None:
        raise TypeError("No input number")

    tmp = round(math.sqrt(n))
    
