from itertools import combinations_with_replacement #중복 조합 함수

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list = sorted(N_list) #순서대로 나오게 정렬 먼저

for numbers in list(combinations_with_replacement(N_list, M)):
    for num in numbers:
        print(num, end=' ')
    print()