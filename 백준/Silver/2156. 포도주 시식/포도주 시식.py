import sys

input = sys.stdin.readline

n = int(input().rstrip())
s = [0] * 10000
for i in range(n):
    s[i] = int(input().rstrip())
dp = [0] * (10000)


dp[0] = s[0] # 수동 계산
dp[1] = s[0] + s[1] # 수동 계산
dp[2] = max(s[0]+s[2], s[2]+s[1], dp[1])
for i in range(3, n):
    # 연속해서 3잔을 못마시도록 
    dp[i] = max(s[i]+dp[i-2], s[i]+s[i-1]+dp[i-3], dp[i-1])
print(max(dp))