import sys
from collections import deque

input = sys.stdin.readline

def bfs(v): # v: 탐색할 그래프 
    q = deque([1]) # 인접 노드를 저장할 큐 

    while q:
        node = q.popleft()
        graph[node].sort() # 내림차순으로 방문 

        # 방문한 노드의 주변 노드를 큐에 삽입 
        for neighbor in graph[node]:
            # 아직 방문하지 않은 주변 노드일 경우 
            if visited[neighbor] == 0:
                visited[neighbor] = 1 # 방문 표시시
                q.append(neighbor) # 큐에 추가

n = int(input().rstrip()) # 컴퓨터 개수
m = int(input().rstrip()) # 노드 개수 
graph = [[] for _ in range(n+1)] # 그래프 초기화 
visited = [0] * (n+1) # 방문 여부를 확인할 리스트

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v) # 그래프 u에 v를 연결
    graph[v].append(u) # 그래프 v에 u를 연결 

visited[1] = 1 # 1번 컴퓨터부터 방문이기에 1을 표시

bfs(graph)
print(sum(visited)-1)
