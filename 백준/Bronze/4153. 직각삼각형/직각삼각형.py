while True:
    l = list(map(int, input().split()))
    if l == [0, 0, 0]:
        break
    else:
        l.sort()
        if l[2]**2 == l[1]**2 + l[0]**2:
            print('right')
        else:
            print('wrong')