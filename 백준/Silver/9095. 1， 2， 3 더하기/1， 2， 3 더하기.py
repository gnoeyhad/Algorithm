import sys

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    a = int(input().rstrip())
    dp = [0]*(a+1)

    for i in range(1, a+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[a])

