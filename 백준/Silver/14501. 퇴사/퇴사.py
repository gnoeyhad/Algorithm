import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
t = [0]
p = [0]

for _ in range(n):
    m, k = map(int, input().rstrip().split())
    t.append(m)
    p.append(k)

dp = [0]*(n+6)

for i in range(n, 0, -1): # 뒤에서부터 거꾸로 계산하기 
    if i+t[i] > n+1: # 날짜를 초과한 경우 
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])

print(dp[1])