# fun old quick sort
# pivot
# works for pivot = last element
# generalize it

def partition(A, l, r):
    # take the pth element in the Array A and put it in the 
    # correct position in A (ascending)
    i = l
    pivot = A[l]
    for j in range(l+1,r+1,1):
        if pivot > A[j]:
            i=i+1
            A[i] , A[j] = A[j], A[i] 
        
    A[i] , A[l] = A[l], A[i] 
    return i

def quick_sort(A, l, r):
    if l<r:
        p = partition(A, l, r)
        quick_sort(A, l, p-1)
        quick_sort(A, p+1, r)
    return A
print(quick_sort([8 ,9, 10, 1, 2, 3, 4, 5], 0, 7))

# note : first and last elements works for pivot
# needs sone special tweaking for each
# for any random pivot - replace with the front or last to make it work
