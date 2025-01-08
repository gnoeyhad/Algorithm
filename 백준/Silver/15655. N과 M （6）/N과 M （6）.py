import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().rstrip().split())
l = [*map(int, sys.stdin.readline().rstrip().split())]
l.sort()
for i in combinations(l, m):
    for j in i:
        print(j, end=' ')
    print()
