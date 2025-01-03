import sys
from collections import deque 

n = int(sys.stdin.readline().rstrip())
q = deque()

for i in range(n):
    l = sys.stdin.readline().rstrip().split()

    if l[0] == 'push':
        q.append(int(l[1]))

    elif l[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    elif l[0] == 'back':
        if q:
            print(q[len(q)-1])
        else:
            print(-1)

    elif l[0] == 'size':
        print(len(q))

    elif l[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif l[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)