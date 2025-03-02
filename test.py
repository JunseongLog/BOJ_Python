from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0  # 적합한 값 카운트

for i in range(1, N+1):
    # 1개짜리 부분수열부터 N개짜리 부분수열까지 모두 확인
    for cur in combinations(arr, i):
        if sum(cur) == S:
            count += 1

print(count)