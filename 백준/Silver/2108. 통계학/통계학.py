from collections import Counter

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l.sort()

print(int(round(sum(l)/n, 0)))

print(l[n//2])

counter = Counter(l)
b = counter.most_common() #최빈값 튜플

if n>1:
    if b[0][1] == b[1][1]:
        print(b[1][0])
    else:
        print(b[0][0])
else:
    print(l[0])
        
print(max(l)-min(l))