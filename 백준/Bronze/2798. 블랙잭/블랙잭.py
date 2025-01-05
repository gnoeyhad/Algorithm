import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().rstrip().split())
l = [*map(int, sys.stdin.readline().rstrip().split())]
dif = {}

for i in list(combinations(l, 3)):
    j = sum(i)
    if j > m:
        continue
    else:
        dif[j]=m-j
print(min(dif, key=dif.get))
    