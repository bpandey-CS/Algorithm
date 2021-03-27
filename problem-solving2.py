#!/bin/python3

"""
non recursive approach for problem-solving1.py
"""

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
# let's try a non recursive approach
def jumpingOnClouds(c):
    pathlen = 0
    if len(c)==0 : return 0
    if len(c)==1 : return 0
    
    while(len(c)>2):
        if c[2]==0 : 
            pathlen = pathlen + 1
            c = c[2:]
        elif c[2]==1 : 
            pathlen = pathlen + 1
            c = c[1:]
        
    if len(c)>1 : pathlen = pathlen + 1 
    
    return pathlen
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
