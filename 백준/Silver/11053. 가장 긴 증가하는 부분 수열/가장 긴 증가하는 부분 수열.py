import sys

input = sys.stdin.readline

n = int(input().rstrip())
s = [*map(int, input().rstrip().split())]

dp = [1] * n

for i in range(1, n): # 현재 탐색 중: i
    for j in range(i): # i보다 앞에 있는 애들을 탐색하는 순서로 진행하기 위함
        if s[i] > s[j]: # 현재 탐색 중인 i보다 그 앞에 있는 숫자가 큰 경우  
            dp[i] = max(dp[i], dp[j]+1) # 더 길게 이어진 것을 dp[i]로 설정

print(max(dp))