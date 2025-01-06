import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().rstrip().split())
l = [*map(int, sys.stdin.readline().rstrip().split())]

ll = list(set(permutations(l, m)))
ll.sort()

for i in ll:
    for j in i:
        print(j, end=' ')
    print()
    
    