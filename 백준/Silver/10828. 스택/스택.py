n = int(input())
st = []
for i in range(n):
    l = input().split()
    if l[0] == 'push':
        st.append(int(l[1]))
    elif l[0] == 'top':
        if st:
            print(st[len(st)-1])
        else:
            print(-1)
    elif l[0] == 'size':
        print(len(st))
    elif l[0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == 'pop':
        if st:
            print(st[len(st)-1])
            del st[len(st)-1]
        else:
            print(-1)