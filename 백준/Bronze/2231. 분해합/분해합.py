Test_num = int(input())
answer = 0

for i in range(1, Test_num+1):
    if i >= 10:
        i_str = list(str(i))
        result = i
        for j in i_str:
           result += int(j)
        if result == Test_num:
            answer = i
            break
    else:
        if Test_num == i+i:
            answer = i
print(answer)