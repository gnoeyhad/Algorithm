def func_bin(x):
    li = []
    res = ''
    
    while(x):
        li.append(x%2)
        x = x // 2
    
    for i in range(len(li)-1, -1, -1):
        res += str(li[i])
    
    return res

def solution(s):
    answer = []
    cnt_z_tot = 0
    cnt_turn = 0
    
    while(s != "1"):
        cnt_z = 0
        for i in s:
            if i == '0':
                cnt_z += 1
        cnt_z_tot += cnt_z
        bin = len(s)-cnt_z # 0 제거 후 길이
        s = func_bin(bin)
        cnt_turn += 1 
    
    return [cnt_turn, cnt_z_tot]