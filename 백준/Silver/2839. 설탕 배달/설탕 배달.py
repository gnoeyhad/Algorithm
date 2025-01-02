n = int(input())
p = 0

if n%5==0:
    print(n//5)
else:
    while n > 0:
        n -= 3 # 3kg 빼기
        p += 1 # 1봉투 추가
        if n%5 == 0: # 3, 5로 조합해서 담을 수 있을 때
            p += n//5
            print(p)
            break
        elif n==1 or n==2:
            print(-1)
            break
        elif n==0: # 3으로 나누어떨어지는 경우
            print(p)
            break
