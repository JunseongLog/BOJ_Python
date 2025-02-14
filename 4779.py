# 백준 4779번 칸토어 집합

# 재귀함수 사용 코드
def function(N):

    if N == 0:
        return "-"
    
    return function(N-1) + (" " * ( 3 ** (N-1))) + function(N-1)

while True:
    try:
        N = int(input())
        print(function(N))
    except:
        break

"""
# 반복문 사용 코드
array = ["" for _ in range(13)]
array[0] = "-"

for i in range(1, 13):
    array[i] = array[i-1] + (" " * (3 ** (i-1))) + array[i-1]

while True:
    try: # try-except 구문 - 예외처리시 사용용
        N = int(input())
        print(array[N])
    except: # 더 받을 값이 없으면 탈출
        break
"""