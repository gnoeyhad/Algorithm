import sys
n = int(sys.stdin.readline().strip())
s = []

for i in range(n):
    l = sys.stdin.readline().strip().split()
    if len(l)==2:
        a, b = l[0], int(l[1])
    else:
        a = l[0]

    if a == 'add':
        if b in s:
            continue
        else:
            s.append(b)
    elif a == 'check':
        if b in s:
            print(1)
        else:
            print(0)
    elif a == 'all':
        s = [i for i in range(1, 21)]
    elif a == 'empty':
        s = []
    elif a == 'remove':
        if b in s:
            s.remove(b)
        else:
            continue
    elif a == 'toggle':
        if b in s:
            s.remove(b)
        else:
            s.append(b)