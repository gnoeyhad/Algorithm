import sys
n = (sys.stdin.readline().rstrip())
num = '369'
cnt = 0
for i in range(1, int(n)+1):
    for j in str(i):
        if j in num:
            cnt+=1
print(cnt)