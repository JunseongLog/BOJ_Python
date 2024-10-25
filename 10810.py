# BOJ 10810번 공 넣기

n, m = map(int, input().split())
bag = [0] * n

for i in range(m):
    start, end, number = map(int, input().split())

    for j in range(start - 1, end):
        bag[j] = number

for i in range(n):
    print(bag[i], end=" ")