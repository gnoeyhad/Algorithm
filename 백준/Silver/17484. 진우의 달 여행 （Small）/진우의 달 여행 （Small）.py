import sys

input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

visited = [[0]*n]*m

def dfs(x, y, depth, direction, cnt):
    global money
    if depth == n:
        money = min(money, cnt)
        return
    
    for i in range(3): # 3가지 방향으로 탐색 
        if direction == i: # 같은 방향인 경우 
            continue

        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<=n-1 and 0<=ny<=m-1: # 범위 안에 속할 때
            dfs(nx, ny, depth+1, i, cnt+graph[nx][ny]) # backtracking 수행
    
    return


dx = [1, 1, 1] # 대각선 왼쪽 아래, 아래, 대각선 오른쪽 아래 
dy = [-1, 0, 1]
money = 600 # 최소값을 저장할 변수 

for i in range(m):
    dfs(0, i, 1, -1, graph[0][i])

print(money)
