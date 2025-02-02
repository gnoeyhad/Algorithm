import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    kind = int(input().rstrip())
    coins = list(map(int, input().rstrip().split()))
    coins.sort()
    m = int(input().rstrip())

    dp = [0]*(m+1) 
    dp[0] = 1

    for c in coins:
        for i in range(c, m+1): 
            dp[i] += dp[i-c]

    print(dp[m])