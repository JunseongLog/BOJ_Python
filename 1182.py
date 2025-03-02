# 백준 1182번 부분수열의 합

from itertools import combinations

N, S = map(int, input().split())
arr = input().split()
count = 0 # 적합한 값 카운트트

for i in range(1, N+1):
    # 1개짜리 부분수열부터 5개짜리 부분수열까지 모두 확인인
    for cur in combinations(arr, i): # 그래서 여기에 i
        total_sum = 0 # 부분수열의 값을 더해서 저장할 변수

        # 부분수열의 합 구하기기
        for j in range(i):
            total_sum += int(cur[j])
        
        if total_sum == S:
            count += 1

print(count)