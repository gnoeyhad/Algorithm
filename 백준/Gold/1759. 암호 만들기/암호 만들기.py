import sys
from itertools import combinations

ja = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
mo = ('a','e','i','o','u')
n, m = map(int, sys.stdin.readline().rstrip().split())
l = list(set(sys.stdin.readline().rstrip().split()))
l.sort()

for i in combinations(l, n):
    check = False
    cnt = 0
    for j in i:
        if j in mo:
            check = True
    for k in i:
        if k in ja:
            cnt += 1
    if check==True and cnt>=2:
        print(''.join(i))