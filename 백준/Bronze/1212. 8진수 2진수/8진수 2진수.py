import sys
n = int(sys.stdin.readline().rstrip())

if n==0:
    print(0)
else:

    s = []
    for i in str(n):
        a=list(bin(int(i))[2:])
        b = []
        if len(a) == 2:
            a.insert(0, 0)
        elif len(a) == 1:
            a.insert(0, 0)
            a.insert(0, 0)
        s.append("".join(map(str,a)))
    st = "".join(map(str, s))
    print(st.lstrip('0'))