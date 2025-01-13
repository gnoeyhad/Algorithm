import sys
from itertools import product

n, m = map(int, sys.stdin.readline().rstrip().split())
l = list(map(int, sys.stdin.readline().rstrip().split()))
l = sorted(l)

for i in list(product(l, repeat=m)):
    for j in i:
        print(j, end=' ')
    print()

