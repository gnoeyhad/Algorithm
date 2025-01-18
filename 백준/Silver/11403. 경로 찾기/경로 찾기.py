import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
graph = [ list(map(int,input().rstrip().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
            
for row in graph:
    print(' '.join(map(str, row)))