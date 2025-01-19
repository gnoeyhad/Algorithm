import sys

input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

for i in range(1, n): 
    for j in range(len(graph[i])):
        if j == 0: # 각 라인의 맨 처음(바로 위 숫자 더하기)
            graph[i][0] += graph[i-1][0] 
        elif j == i: # 각 라인의 맨 마지막(바로 위 숫자 더하기)
            graph[i][j] += graph[i-1][j-1]
        else: # 왼쪽 대각선, 오른쪽 대각선 중 최댓값을 저장
            graph[i][j] += max(graph[i-1][j-1], graph[i-1][j]) 

print(max(graph[n-1]))