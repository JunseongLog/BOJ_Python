# 백준 2210번 숫자판 점프

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# DFS 사용자함수
def DFS(y, x, string):
    global result

    if len(string) == 6:
        result.append(string)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            DFS(ny, nx, string + str(number_map[ny][nx]))



# 0. 입력 및 초기화
number_map = []
result = []

# 1. 맵 정보 입력
for i in range(5):
    number_map.append(list(map(int, input().split())))

# 2. DFS호출
for i in range(5):
    for j in range(5):
        value = str(number_map[i][j])
        DFS(i, j, value)

# 3. 출력
result = set(result) # 중복걸러주기
print(len(result))