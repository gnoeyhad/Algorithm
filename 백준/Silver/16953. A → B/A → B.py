import sys
a, b = map(int, sys.stdin.readline().rstrip().split())

cnt = 1

while True:
    if a==b:
        break
    elif a>b:
        cnt = -1
        break
    elif b%10==1:
        cnt+=1
        b//=10
    elif b%2==0:
        cnt+=1
        b//=2
    else:
        cnt = -1
        break

print(cnt)