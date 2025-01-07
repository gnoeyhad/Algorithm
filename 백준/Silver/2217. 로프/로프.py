import sys

n = int(sys.stdin.readline().rstrip())
l =[]
for _ in range(n):
    l.append(int(sys.stdin.readline().rstrip()))

max = 0

l.sort()
for i in range(n):
    l[i] = l[i]*(n-i)
    if max < l[i]:
        max = l[i]

print(max)
    