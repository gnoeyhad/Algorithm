n = int(input())
l = list(map(int, input().split()))
total = 0
l.sort()
for i in range(n):
    sum = 0
    for j in range(i+1):
        sum += l[j]
    total += sum

print(total)
