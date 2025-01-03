import sys

n, m = map(int, sys.stdin.readline().split())
l = [*map(int, sys.stdin.readline().split())]


tmp = sum(l[:m])
max = tmp
cnt = 1

for i in range(m, n):
    tmp -= l[i-m]
    tmp += l[i]
    if max < tmp:
        max = tmp
        cnt = 1
    elif max == tmp:
        cnt += 1

if max == 0:
    print('SAD')
else:
    print(max)
    print(cnt)