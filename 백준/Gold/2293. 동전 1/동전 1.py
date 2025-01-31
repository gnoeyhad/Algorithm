import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort()

dp = [0]*(m+1) 
dp[0] = 1

for c in coins:
    for i in range(c, m+1): 
        dp[i] += dp[i-c]

print(dp[m])