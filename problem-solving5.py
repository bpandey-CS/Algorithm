"""
https://www.hackerrank.com/challenges/equality-in-a-array/
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    if len(arr) == len(set(arr)):
        return len(arr) - 1
    else:
        count = {}
        maxm = -math.inf 
        j = -999
        for i in arr:
            count[i] = count.get(i,0) + 1
            if count.get(i) > maxm:
                maxm = count.get(i)
                j = i
        return sum([count.get(i) for i in set(arr) if i != j])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
