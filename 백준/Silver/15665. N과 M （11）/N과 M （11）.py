import sys
from itertools import product

n, m = map(int, sys.stdin.readline().rstrip().split())
l = list(set(map(int, sys.stdin.readline().rstrip().split())))
l.sort()


for i in list(product(l, repeat=m)):
    print(' '.join(map(str, i)))

