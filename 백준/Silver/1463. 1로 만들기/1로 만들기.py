import sys

input = sys.stdin.readline

n = int(input().rstrip())
dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # 나누어 떨어지지 않는 경우는 무조건 1을 빼줌 
                        # 여기서 +1은 횟수를 의미
    if i%3 == 0: # i//3에서 연산했던 것 +1(3으로 또 나눔)이랑 1을 빼서 연산한 dp[i] 중 최솟값을 저장
        dp[i] = min(dp[i//3]+1, dp[i]) 
    if i%2 == 0: # i//2에서 연산했던 것 +1(2으로 또 나눔)이랑 1을 빼서 연산한 dp[i] 중 최솟값을 저장
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[n])