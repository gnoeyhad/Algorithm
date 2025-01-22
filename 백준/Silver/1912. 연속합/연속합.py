import sys
input = sys.stdin.readline

n = int(input().rstrip())
x = list(map(int, input().rstrip().split()))
 
for i in range(1, n):
    x[i] = max(x[i], x[i] + x[i - 1])
 
print(max(x))