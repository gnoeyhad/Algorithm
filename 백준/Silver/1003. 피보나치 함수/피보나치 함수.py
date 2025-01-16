import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    m = int(input().rstrip())
    a, b = 1, 0
    for i in range(m):
        a, b = b, a+b
    print(a, b)
