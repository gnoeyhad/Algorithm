n = int(input())

for i in range(n):    
    answer = True
    st = []
    s = input()
    for i in s:
        if i == '(':
            st.append('(')
        else:
            if st == []:
                answer = False
            else:
                st.pop()
    
    if st != []:
        answer = False
    
    if answer:
        print('YES')
    else:
        print('NO')