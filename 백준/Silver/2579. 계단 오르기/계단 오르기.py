import sys

input = sys.stdin.readline

n = int(input().rstrip())
s = [int(input().rstrip()) for _ in range(n)]
dp = [0] * (n)

if len(s)<=2:
    print(sum(s))
else:
    dp[0] = s[0] # 수동 계산
    dp[1]= s[0] + s[1] # 수동 계산
    for i in range(2, n):
        # 아래 식을 통해서 3칸 연속 뛸 수 없도록 제어
        dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[-1])
    

