# BOJ 1159번 농구 경기

n = int(input())
alpha = [0] * 26

for i in range(n):
    s = input()
    j = ord(s[0]) - ord("a")
    alpha[j] += 1

# 5개 이상인 문자  출력
for i in range(26):
    if alpha[i] >= 5:
        value = chr(i + ord("a"))
        print(value, end="")

# 5개 이상 문자가 하나도 없을 때
if all(value < 5 for value in alpha):
    print("PREDAJA")