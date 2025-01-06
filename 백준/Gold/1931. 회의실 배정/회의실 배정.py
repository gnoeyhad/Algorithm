import sys
n = int(sys.stdin.readline().rstrip())
l = []
for _ in range(n):
    l.append([*map(int, sys.stdin.readline().rstrip().split())])

l.sort(key=lambda x: [x[1], x[0]]) #끝나는 시간을 기준으로 오름차순

end_time = l[0][1]
res = 1

for i in range(1, n):
    start_time = l[i][0]
    if start_time < end_time:
        continue
    end_time = l[i][1]
    res += 1

print(res)