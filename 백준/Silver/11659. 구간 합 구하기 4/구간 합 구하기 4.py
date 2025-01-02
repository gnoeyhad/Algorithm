import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

cumsum = [0]
sum = 0
for i in range(n):
    sum += l[i]
    cumsum.append(sum)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a==b:
        print(l[a-1])
    else:
        print(cumsum[b]-cumsum[a-1])