import sys
input = sys.stdin.readline

n = int(input().rstrip())

l = [1 for _ in range(n+2)]

if n >= 2:
    for i in range(3, n+2):
        l[i] = 2*l[i-2]+l[i-1]

print(l[-1]%10007)
