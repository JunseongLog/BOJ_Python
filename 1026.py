# 백준 1026번 보물

# 순열 기능 Import
from itertools import permutations

# N 입력
N = int(input())

# a, b 각 배열 입력력
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

sum = 0
for i in range(N):
    sum += a[i]*b[i]

print(sum)