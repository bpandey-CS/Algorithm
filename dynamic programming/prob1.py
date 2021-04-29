"""
M X N (m rows n ,cols)

movement ->  right
movement ->  down

no of ways to reach
(1x1) -> 00 1
(2x2) -> 2
(3x3) -> 4
-  -  -  -  -
00 01 02
10 11 12
20 21 22
-  -  -  -  -(m,n)
"""
# iterative approach
dp = [[0]*n for i in range(m)]
for i in range(n):
    dp[0][i] = 1
    
for i in range(m):
    dp[i][0] = 1
    
for i in range(1,m):
    for j in range(n):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]


# recursive approach --> weird but ok

m = 3
n = 8
dt = [[0]*n for i in range(m)]
def path(i,j):
    if i>m-1 or j>n-1:
        return 0
    if dt[i][j] != 0:
        return dt[i][j]
    if i==m-1 and j==n-1:
        return 1
    dt[i][j] = path(i+1,j) + path(i,j+1)
    
    return dt[i][j]
    
print(path(0,0))
print(dt)