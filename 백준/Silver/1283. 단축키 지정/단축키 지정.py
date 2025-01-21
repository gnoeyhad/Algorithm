import sys

input = sys.stdin.readline
n = int(input().rstrip())
dan = []

for _ in range(n):
    flag = False
    key = input().rstrip().split()

    for i in range(len(key)): # 첫 문자자가 단축키에 없는 경우
        if key[i][0].upper() not in dan:
            dan.append(key[i][0].upper())
            flag = True
            key[i] = '['+key[i][0]+']'+key[i][1:]
            print(' '.join(key))
            break
    
    if not flag: # 첫 문자자가 단축키에 있는 경우 
        for i in range(len(key)):
            check = False
            for j in range(len(key[i])):
                if key[i][j].upper() not in dan:
                    dan.append(key[i][j].upper())
                    flag = True
                    check = True
                    key[i] = key[i][:j] + '[' + key[i][j] + ']' + key[i][j+1:]
                    print(' '.join(key))
                    break
            if check:
                break
    
    if not flag: # 모든 글자들이 단축키에 있는 경우 
        print(' '.join(key)) # 그대로 출력 