N = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]


for i in range(1,N+1):
    for k in range(1,i+1):
         # 현재 구한 최댓값 dp[i]와 i-k개의 카드를 구매할 때 
         # 최대인 dp[i-k]와 p[k]를 더해서 최댓값 비교 
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])