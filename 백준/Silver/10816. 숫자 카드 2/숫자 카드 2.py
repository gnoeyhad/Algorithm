import sys

n = sys.stdin.readline().strip()
card = list(map(int, sys.stdin.readline().strip().split()))
m = input()
l = list(map(int, sys.stdin.readline().strip().split()))

count = {}
for i in card:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in l:
    res = count.get(i) # 키 조회
    if res == None:
        print(0, end=' ')
    else:
        print(res, end=' ')