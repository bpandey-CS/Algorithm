import cProfile

def func(n):
    for i in range(1,11):
        count_j = 0
        count_k = 0
        for j in range(1, (i+1)**2):
            count_j = count_j + 1
            for k in range(1, (n//2)+1):
                count_k = count_k + 1
        print("iteration i = {}".format(i))
        print("j = {}".format(count_j))
        print("k = {}\n".format(count_k))

cProfile.run('func(10)')