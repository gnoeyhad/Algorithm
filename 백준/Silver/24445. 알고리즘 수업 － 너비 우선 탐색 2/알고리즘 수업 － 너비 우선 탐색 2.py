import sys
from collections import deque

input = sys.stdin.readline

def bfs(v): # v: 탐색할 그래프 
    order = 1
    q = deque([v]) # 인접 노드를 저장할 큐 
    visited[v] = order # 시작 노드 방문 

    while q:
        node = q.popleft()
        graph[node].sort(reverse=True) # 내림차순으로 방문 

        # 방문한 노드의 주변 노드를 큐에 삽입 
        for neighbor in graph[node]:
            # 아직 방문하지 않은 주변 노드일 경우 
            if visited[neighbor] == 0:
                order += 1
                visited[neighbor] = order # 방문
                q.append(neighbor) # 큐에 추가

n, m, r = map(int, input().rstrip().split())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1) # 방문 여부를 확인할 리스트

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)


bfs(r)

for i in range(1, n+1):
    print(visited[i])