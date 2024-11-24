# 백준 1388번 바닥 장식

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(y, x, type):
    global floor_map
    # visited 없이 맵에 방문처리
    floor_map[y][x] = 0

    if type == "-":
        
        if 0 <= (x+1) < M and floor_map[y][x+1] == type:
            DFS(y, x+1, type)
    elif type == "|":

        if 0 <= (y+1) < N and floor_map[y+1][x] == type:
            DFS(y+1, x, type)




# 0. 입력 및 초기화
N, M = map(int, input().split()) #N세로 M가로
floor_map = []
cnt = 0

# 1. 연결 정보 입력
for i in range(N):
    # 다 붙여서 입력을 받을때는 rstrip으로 오른쪽 공백을 빼고 받아야함
    floor_map.append(list(input().rstrip()))

# 2. DFS호출

for i in range(N):
    for j in range(M):
        if floor_map[i][j] == "-":
            DFS(i, j, "-")
            cnt += 1
        elif floor_map[i][j] == "|":
            DFS(i, j, "|")
            cnt += 1

# 3. 출력
print(cnt)