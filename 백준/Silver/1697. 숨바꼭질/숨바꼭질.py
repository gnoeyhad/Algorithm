import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
max = 10 ** 5 # 움직일 수 있는 최대 좌표
visited = [0] * (max+1)

# bfs
def bfs():
    q = deque()
    q.append(n) # 수빈이의 출발 지점

    while q:
        x = q.popleft()
        if x == m: # 만약 동생의 위치가 같다면
            print(visited[x])
            break
        # 이동 방향 계산
        for j in (x+1, x-1, x*2):
            if 0 <= j <= max and visited[j] == 0: # 범위 내에 있고 방문 안한 상태라면
                visited[j] = visited[x] + 1 # 이동 시간 표시 
                q.append(j)

bfs()