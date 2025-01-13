import sys
from itertools import permutations


n = int(sys.stdin.readline().rstrip())
l = [i for i in range(1, n+1)]

for i in permutations(l, n):
    for j in i:
        print(j, end=' ')
    print()