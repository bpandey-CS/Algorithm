# subset max multiply

def subset_mult(A, v):
    A.sort()
    
    for p in range(len(A)):
        if A[p] > 0:
            break
    is_odd = 0 if p%2 == 0 else 1 
    l = 0
    r = len(A) - 1
    mult = 1
    while(v > 0):
        mult_l = A[l] * A[l+1]
        mult_r = A[r] * A[r-1]
        if mult_r > mult_l and r > p:
            mult = mult * mult_r
            print(A[r-1]," ", A[r])
            r = r - 2 
            v = v - 2
        elif l < (p + is_odd):
            mult = mult * mult_l
            print(A[l]," ", A[l+1])
            l = l + 2
            v = v - 2
    
    return mult

print(subset_mult([7,6,5,-5,-4,-3,-6], 4))
        