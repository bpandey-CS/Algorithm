# subset sum
# we will be given a set of numbers and a sum
# say yes or not if that sum can be obtained or not
[1, 2, 3, -4, -2, -1]
def subset_sum(A, n):
    rows = len(A) + 1
    columns = n + 1
    ss[]