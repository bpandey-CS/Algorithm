# dynamic approach verification
# sum of first n fibonacci numbers
import cProfile

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

# find a way to do the recursion using iteration
def fib_dyn(n):
    a = [0] * n
    a[0] = 0
    a[1] = 1
    for i in range(2, n):
        a[i] = a[i-1] + a[1-2]
    return a[n-1]

print("Fib without dynamic approach")
cProfile.run('fib(10)')
print("Fib without dynamic approach")
cProfile.run('fib_dyn(10)')