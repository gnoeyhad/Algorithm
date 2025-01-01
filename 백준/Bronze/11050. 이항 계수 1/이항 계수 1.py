def fact(a):
    sum = 1
    for i in range(1, a+1):
        sum *= i
    return sum

n, k = map(int, input().split())

print(int(fact(n)/fact(n-k)/fact(k)))