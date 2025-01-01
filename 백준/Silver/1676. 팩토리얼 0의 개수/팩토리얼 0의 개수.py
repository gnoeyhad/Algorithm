def fact(a):
    sum = 1
    for i in range(1, a+1):
        sum *= i
    return str(sum)

n = fact(int(input()))
cnt = 0

for i in range(len(n)-1, -1, -1):
    if n[i] == '0':
        cnt += 1
    else:
        break
print(cnt)