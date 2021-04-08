"""
=begin
  Define f(n) as the sum of the factorials of the digits of n. For example, f(342) = 3! + 4! + 2! = 32.
  Define sf(n) as the sum of the digits of f(n). So sf(342) = 3 + 2 = 5.
  Define g(i) to be the smallest positive integer n such that sf(n) = i. Though sf(342) is 5, sf(25) is also 5, and it can be verified that g(5) is 25.
  Define sg(i) as the sum of the digits of g(i). So sg(5) = 2 + 5 = 7.
  Further, it can be verified that g(20) is 267 and  sg(i) for 1  i  20 is 156.
  What is sum(sg(i)) for 1<=i<=150?
=end
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
fact = {
    0:1,
    1:1,
    2:2,
    3:6,
    4:24,
    5:120,
    6:720,
    7:5040,
    8:40320,
    9:362880,
    10:3628800
}
n = 0

def sum_of_digits(n):
    return sum(list(map(int, str(n))))
    
def f(i):
    if i == 0:
        return 0
    return sum([fact[n] for n in list(map(int, str(i)))])

def sf(i):
    n = f(i)
    return sum_of_digits(n)

def g(i):
    global n
    n2 = 0
    while(True):
        n2 = sf(n)
        if n2 == i:
            return n
        n = n + 1

def sg(i):
    n = g(i)
    return sum_of_digits(n)

# no_of_exec = int(input())
# for _ in range(no_of_exec):
#     inp = list(map(int, input().split()))
#     n = inp[0]
#     m = inp[1]
#     s = 0
#     for i in range(1,n+1):
#         s = s + sg(i)
#     print(s%m)
    
for i in range(1, 151):
    print("#################")
    print(i)
    print(sg(i))
    print(n)
# print(sg(41))
# from pprint import pprint
# pprint(d)
# filehandler = open(filename, 'wb')
# pickle.dump(dictionary, filehandler)