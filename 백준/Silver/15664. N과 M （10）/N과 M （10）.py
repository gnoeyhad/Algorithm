import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
l = list(map(int, sys.stdin.readline().rstrip().split()))
l = sorted(l)
k = []

for i in list(combinations(l, m)):
    if i not in k:
        k.append(i)

for j in k:
    for h in j:
        print(h, end=' ')
    print()
