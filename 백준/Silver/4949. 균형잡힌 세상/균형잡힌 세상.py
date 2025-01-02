

while True:    
    answer = True
    st = []
    s = input()
    if s == '.':
        break
    else:
        for i in s:
            if i == '(':
                st.append('(')
            elif i == '[':
                st.append('[')
            elif i == ')':
                if st == []:
                    answer = False
                elif st[-1] == '(':
                    st.pop()
                else:
                    answer = False

            elif i == ']' :
                if st == []:
                    answer = False
                elif st[-1] == '[':
                    st.pop()
                else:
                    answer = False

            else:
                continue
      
        
        if st != []:
            answer = False
        
        if answer:
            print('yes')
        else:
            print('no')