import sys
from heapq import heappush, heappop 

input = sys.stdin.readline

n = int(input().rstrip())
q = [] # 최소 힙으로 사용 

for _ in range(n):
    a = int(input().rstrip())
    if a == 0: 
        if len(q) == 0:
            print(0)
        else:
            print(heappop(q)) # q에서 최소값 뺌 
    else:
        heappush(q, a) # q에 a를 추가
    