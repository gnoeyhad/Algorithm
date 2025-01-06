import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().rstrip().split())
l = [i for i in range(1, n+1)]
dif = {}

for i in list(permutations(l, m)):
    for j in i:
        print(j, end=' ')
    print()
    
    