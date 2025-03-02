# 백준 2503번 숫자 야구

from itertools import permutations

N = int(input())
infos = [list(input().split()) for _ in range(N)]
ans = 0

# 1부터 9까지 중에서 3개만 뽑아서 순열을 만들고 하나씩 cur에 담는 것
for cur in permutations(range(1, 10), 3):
    ok = True
    
    # 한 값이 모든 조건에 동일하는지 보기위한 for문문
    for num, st, ball in infos:
        actual_st = 0 # 값의 실제 스트라이크 값
        actual_ball = 0 # 값의 실제 볼 값

        # 스트라이크, 볼 확인인
        for i in range(3):
            if num[i] == str(cur[i]): # st일때
                actual_st += 1
            elif str(cur[i]) in num: # ball일때
                actual_ball += 1
        
        # 결과값 대조 확인인
        if actual_st != int(st) or actual_ball != int(ball):
            ok = False
            break # break를 쓰면 한 반복문만 벗어난다.
    
    # 모든 입력값이 일치하면면
    if ok:
        ans += 1
        
print(ans)