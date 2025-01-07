import sys

n = int(sys.stdin.readline().rstrip())

l =[300, 60, 10]
cnt = []

for i in l:
    cnt.append(str(n//i))
    n = n%i

if n != 0:
    print(-1)
else:
    print(' '.join(cnt))