# 백준 10870번 피보나치 수 5

# 재귀 깊이 확장
import sys
sys.setrecursionlimit(10**6)

# Define Function Fibonacci
def Fibonacci(N): 
    # BaseCase
    if N == 0: # 가장 마지막 수가 0이니까
        return N # N은 0 즉, 0을 리턴
    elif N == 1:
        return N # N은 1 즉, 1을 리턴
    # RecursionCase  
    return Fibonacci(N-1) + Fibonacci(N-2)

# 0. 입력
N = int(input())

# 1. Excute Fibonacci Function
print(Fibonacci(N))