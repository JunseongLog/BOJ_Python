# BOJ 11655번 ROT13 

# 아스키코드 값
# 65(A)부터 90(Z)까지
# 97(a)부터 122(z)까지

# 대문자는 대문자 로테이션
# 소문자는 소문자 로테이션

s = input()

# 파이썬은 문자열 변경 불가능하기 때문에 직접 수정할 수 없음
result = []

for char in s:
    # 대문자 일때
    if (char.isupper() == True):
        value = ord(char) + 13
        if value > 90:
            value -= 26
        result.append(chr(value))
    # 소문자 일때
    elif (char.islower() == True):
        value = ord(char) + 13
        if value > 122:
            value -= 26
        result.append(chr(value))
    # 그 외에는 그대로
    else:
        result.append(char)

print("".join(result))



