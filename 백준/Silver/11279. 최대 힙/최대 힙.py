import sys
from heapq import heappush, heappop 

input = sys.stdin.readline

n = int(input().rstrip())
q = [] # 최대 힙으로 사용용 

for _ in range(n):
    a = int(input().rstrip())
    if a == 0: 
        if len(q) == 0:
            print(0)
        else:
            print(-heappop(q)) # 최솟값에다가 *-1 즉, 최대값을 뺌 
    else:
        heappush(q, -a) # q에 -a를 추가 (최대 힙으로 사용하기 위해해)
    