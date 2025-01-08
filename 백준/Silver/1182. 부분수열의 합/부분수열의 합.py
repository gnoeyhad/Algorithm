import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().rstrip().split())
l = [*map(int, sys.stdin.readline().rstrip().split())]

cnt = 0
for i in range(n):
    
    perm  = combinations(l, i+1)
    for j in perm:
        tot = 0
        for k in j:
            tot+=k
        if tot==s:
            cnt+=1
    
   
print(cnt)