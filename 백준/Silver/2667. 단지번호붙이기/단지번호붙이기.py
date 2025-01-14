import sys
from collections import deque 
input = sys.stdin.readline

graph = []

n = int(input().rstrip())
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

#너비 우선 탐색 bfs
def bfs(graph, x, y):
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    graph[x][y] = 0 # 방문한 집은 0으로 바꾸기
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어난 경우
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            # 집을 발견한 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 다시 방문하지 않도록 변경
                queue.append((nx, ny))
                cnt += 1

    return cnt

# graph의 값이 1인 경우 탐색 진행
count = [bfs(graph, i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]

count.sort()
print(len(count))

for i in count:
    print(i)