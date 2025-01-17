import sys

input = sys.stdin.readline

n = int(input().rstrip())
s = [*map(int, input().rstrip().split())]

dp = [0] * n # 증가하는 부분 수열의 개수를 구하는 배열 
dp[0] = s[0]

for i in range(0, n): # 현재 탐색 중: i
    for j in range(i): # i보다 앞에 있는 애들을 탐색하는 순서로 진행하기 위함
        if s[i] > s[j]: # 현재 탐색 중인 i가 그 앞에 있는 숫자가 큰 경우  
            dp[i] = max(dp[i], dp[j]+s[i]) # 합을 비교하여 더 큰 값을 넣음
        else: # 숫자가 같은 경우 
            dp[i] = max(dp[i], s[i]) # 둘 중 큰 값을 dp로 대입

print(max(dp))