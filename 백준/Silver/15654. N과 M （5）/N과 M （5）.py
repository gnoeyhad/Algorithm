import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().rstrip().split())
l = [*map(int, sys.stdin.readline().rstrip().split())]
l.sort()
for i in list(permutations(l, m)):
    for j in i:
        print(j, end=' ')
    print()
    
    