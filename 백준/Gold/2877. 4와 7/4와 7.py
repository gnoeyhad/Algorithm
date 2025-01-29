import sys
n = int(input().rstrip())
res = ''
while n > 0:
    m = n%2
    n = n//2
    if m == 0: # 짝수인 경우 
        n -= 1 # n//2-1로 8: 447인 경우 44를 찾아 다시 계산
        res = '7' + res 
    else: # 홀수인 경우 n//2 를 계산 
        res = '4' + res
print(res)