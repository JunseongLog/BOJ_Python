# 백준 10870번 피보나치 수 5

# 재귀 깊이 확장
import sys
sys.setrecursionlimit(10**6)

# Define Function Fibonacci
def Fibonacci(x):
    global lst

    if lst[x] != -1: # 값이 이미 들어가 있으면 그 값을 리턴
        return lst[x]

    lst[x] = Fibonacci(x-1) + Fibonacci(x-2)
    return lst[x] 

# 0. 입력
N = int(input())

# -1로 초기화 하는 이유는 안 나올만한 값이기 때문문
lst = [-1] * (N+2) # N+2인 이유는 2개의 값을 미리 지정하기 때문, N+1일때 N=0이면 lst[1]에 접근하면 인덱스 오류가남남
lst[0] = 0
lst[1] = 1
# 1. Excute Fibonacci Function
print(Fibonacci(N))