import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline().rstrip()))

l.sort(reverse=True)

count = 0

for i in l:
    count += m//i
    m = m%i
    a=count

print(a)