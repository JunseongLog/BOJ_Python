# BOJ 3986번 좋은 단어

n = int(input())

count = 0
for i in range(n):
    # 파이썬이니 스택 역할을 할 리스트 선언
    stack = []

    s = input()
    for value in s:
        if stack:
            if value == stack[-1]:
                stack.pop()
            else:
                stack.append(value)
        else:
            stack.append(value)
    
    if not stack:
        count += 1

print(count)
