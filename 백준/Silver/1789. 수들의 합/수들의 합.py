import sys
n = int(sys.stdin.readline().rstrip())

tot = 0
count = 0

while True:
    count += 1
    tot += count
    if tot > n:
        break

print(count-1)