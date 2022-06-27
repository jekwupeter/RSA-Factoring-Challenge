#!/usr/bin/python3
import sys
import math

def _fact(n):
    """Finds possible factors of a number
    Args:
        n (int): input natural number
    Returns:
        a list of two integers that multiplies to give input number
    """
    upper_bound = int(math.sqrt(n))
    tmp = list(range(upper_bound, n))
    for i in range(upper_bound, n):
        holder = [None, None]
        if n % i == 0:
            if num in [2, 3, 5, 7, 11, 13, 17]:
                holder[0] = i
                holder[1] = int(n / i)
                return holder
            
            for j in tmp:
                if i % j == 0:
                    tmp.remove(j)
                    break
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

