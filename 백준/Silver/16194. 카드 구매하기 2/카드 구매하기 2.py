N = int(input())
p = [0] + list(map(int,input().split()))
dp = [False for _ in range(N+1)]


for i in range(1,N+1):
    for k in range(1,i+1):
        if dp[i] == False: # 아예 값을 구한 적 없는 경우 
            dp[i] = dp[i-k] + p[k]
        else: # 기존 dp[i]를 구해서 비교해야할 값이 있는 경우 
            dp[i] = min(dp[i], dp[i-k] + p[k]) # 두 값 중 최소를 선택 

print(dp[N]) # 카드 N개를 구매하는 최대 가격 