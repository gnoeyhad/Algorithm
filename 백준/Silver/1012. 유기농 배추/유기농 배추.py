import sys
from collections import deque

input = sys.stdin.readline
turn = int(input().rstrip())

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]

    cnt = 0

    queue = deque()
    queue.append((x, y))

    graph[x][y] = 0 # 방문한 곳은 0으로 변경

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1

    return cnt


for i in range(turn):
    m, n, k = map(int, input().rstrip().split())
    graph = [[0]*n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        graph[x][y] = 1
    

    count = [bfs(graph, i, j) for i in range(m) for j in range(n) if graph[i][j] == 1]

    print(len(count))