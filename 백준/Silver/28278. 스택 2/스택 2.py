import sys

n = int(sys.stdin.readline())
st = []
for i in range(n):
    l = sys.stdin.readline().split()
    if l[0] == '1':
        st.append(int(l[1]))
    elif l[0] == '5':
        if st:
            print(st[len(st)-1])
        else:
            print(-1)
    elif l[0] == '3':
        print(len(st))
    elif l[0] == '4':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == '2':
        if st:
            print(st[len(st)-1])
            del st[len(st)-1]
        else:
            print(-1)