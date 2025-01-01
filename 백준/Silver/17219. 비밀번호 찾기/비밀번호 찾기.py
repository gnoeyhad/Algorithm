n, m = map(int, input().split())
dict = {}

for i in range(n):
    site, pw = input().split()
    dict[site] = pw

for i in range(m):
    search = input()
    print(dict[search])