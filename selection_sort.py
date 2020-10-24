# selection sort 
# very simple look it up
#User function Template for python3
# {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
def select(arr, i):
    # code here 
    max = arr[i]
    j = i
    for k in range(i, -1, -1):
        if arr[k] > max:
            max = arr[k]
            j = k
    return j

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1,0, -1):
        j = select(arr,i)

        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        selectionSort(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends