# BOJ 10988번 팰린드롬인지 확인하기

s = input()

# 반으로 나눠서 앞이랑 뒤를 비교
n = len(s) // 2
# check로 팰린드롬인지 아닌지 구분
check = 0
for i in range(n):
    # 인덱스 값이기 때문에 "(len(s) - 1) - i" 이다
    if s[i] != s[(len(s)-1)-i]:
        check += 1

if check == 0:
    print(1)
else:
    print(0)

    