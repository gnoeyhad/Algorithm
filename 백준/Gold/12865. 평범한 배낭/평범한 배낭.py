import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
bag = []
for i in range(n):
    bag.append([*map(int, input().rstrip().split())])

dp = []

for i in range(n+1):
    dp.append([])
    for c in range(k+1):
        if i==0 or c==0:
            dp[i].append(0)
        elif bag[i-1][0] <= c:
            dp[i].append(
                max(
                    bag[i-1][1] + dp[i-1][c-bag[i-1][0]], 
                    dp[i-1][c]
                )
            )
        else:
            dp[i].append(dp[i-1][c])
    #print(dp)
print(dp[-1][-1])