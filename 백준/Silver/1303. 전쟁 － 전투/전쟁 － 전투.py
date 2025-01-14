import sys
from collections import deque 
input = sys.stdin.readline

graph = []

n, m = map(int, input().rstrip().split())
for _ in range(m):
    graph.append(list(input().rstrip()))

#너비 우선 탐색 bfs
def bfs(graph, x, y, color, cnt=1):
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    graph[x][y] = 0 # 방문한 집은 0으로 바꾸기
    
    while queue:
        
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어난 경우
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue

            # 흰색을 발견한 경우
            if graph[nx][ny] == color:
                graph[nx][ny] = 0 # 다시 방문하지 않도록 변경
                queue.append((nx, ny))
                cnt += 1


    return cnt

# graph의 값이 1인 경우 탐색 진행
w_count = [bfs(graph, i, j, 'W')**2 for i in range(m) for j in range(n) if graph[i][j] == 'W']
b_count = [bfs(graph, i, j, 'B')**2 for i in range(m) for j in range(n) if graph[i][j] == 'B']

print(sum(w_count), sum(b_count))