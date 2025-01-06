import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().rstrip().split())
l = [i for i in range(1, n+1)]
dif = {}

for i in list(combinations_with_replacement(l, m)):
    for j in i:
        print(j, end=' ')
    print()
    
    