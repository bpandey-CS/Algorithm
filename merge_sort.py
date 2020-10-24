# merge sort 
# the fun old merge sort 
import math

def merge(array, p, q, r):
    """
    :Merge sort
        - Array - that needs to be sorted
        - p - starting index of the array
        - q - the split index
        - r - ending index
    """
    # defining two arrays
    a = [0] * (q - p + 1)
    b = [0] * (r - q)
    j = 0
    for i in range(p, q+1, 1):
        a[j] = array[i]
        j = j + 1
    j = 0
    for i in range(q+1, r+1, 1):
        b[j] = array[i]
        j = j + 1
    a.append(math.inf) 
    b.append(math.inf)
    i = 0
    j = 0
    for k in range(0, len(array), 1):
        if (a[i] < b[j]):
            array[k] = a[i]
            i = i + 1
        elif (a[i] >= b[j]):
            array[k] = b[j]
            j = j + 1
    
    return array


def merge_sort(array, p, r):
    if p > r:
        q = (r-p)//2
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q, r)
    else:
        return array

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        p=int(input())
        r=int(input())
        merge_sort(arr, p, r)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
