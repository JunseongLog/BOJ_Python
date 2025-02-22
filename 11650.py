# 백준 11650번 좌표 정렬하기

N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr = sorted(arr, key=lambda x : x)

for x in arr:
    print(x[0],x[1])


# arr = [list(map(int, input().split())) for _ in range(N)]
