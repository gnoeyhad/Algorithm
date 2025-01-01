n = int(input())
l = list(map(int, input().split()))
new_sum = 0
max_score = max(l)
for i in l:
    new_sum += i/max_score*100
print(new_sum/n)