
"""
There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

Example


The substring we consider is , the first  characters of the infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Returns

int: the frequency of a in the substring
Input Format

The first line contains a single string, .
The second line contains an integer, .

Constraints

For  of the test cases, .
Sample Input

Sample Input 0

aba
10
Sample Output 0

7
Explanation 0
The first  letters of the infinite string are abaabaabaa. Because there are  a's, we return .

Sample Input 1

a
1000000000000
Sample Output 1

1000000000000
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    to_repeat = int(n/len(s))
    a_count = sum([1 for st in s if st=='a'])
    a_count = a_count * to_repeat 
    last_s = s[0:(n-(len(s) * to_repeat))]
    a_count = a_count + sum([1 for st in last_s if st=='a'])
    return a_count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
