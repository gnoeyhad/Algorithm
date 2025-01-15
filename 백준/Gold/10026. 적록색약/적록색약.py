import sys
from collections import deque 
input = sys.stdin.readline

#너비 우선 탐색 bfs
def bfs(x, y):
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]

    queue.append((x, y))

    visited[x][y] = 1 
    
    while queue:
        
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고, 아직 방문을 하지 않았고, 같은 색인 경우 큐에 넣기 
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1 
                queue.append((nx,ny))

n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]
queue = deque()

# 적록색약이 아닌 경우 
visited = [[0]*n for _ in range(n)]
cnt_1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt_1 += 1

# 적록색약인 경우
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0]*n for _ in range(n)]
cnt_2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt_2 += 1


print(cnt_1, cnt_2)