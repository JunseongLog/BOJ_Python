# 백준 1303번 전쟁-전투

# 재귀 횟수, 읽는 속도 늘리기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(y, x, type):
    global war_map, white_cnt, blue_cnt, white_list, blue_list
    war_map[y][x] = 0
    
    if type == "W":
        white_cnt += 1
    elif type == "B":
        blue_cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and war_map[ny][nx] == type:
            DFS(ny, nx, type)

# 0. 입력 및 초기화
N, M = map(int, input().split()) # N가로, M세로
war_map = []

white_list = []
blue_list = []

# 1. 연결 정보 입력
for i in range(M):
    war_map.append(list(input().rstrip()))

# 2. DFS호출
for i in range(M):
    for j in range(N):
        if war_map[i][j] == "W":
            white_cnt = 0
            DFS(i, j, "W")
            white_list.append(white_cnt)
        elif war_map[i][j] == "B":
            blue_cnt = 0
            DFS(i, j, "B")
            blue_list.append(blue_cnt)

# 3. 각 값을 제곱
for i in range(len(white_list)):
    white_list[i] = (white_list[i]**2)

for i in range(len(blue_list)):
    blue_list[i] = (blue_list[i]**2)

# 4. 출력

print(sum(white_list), sum(blue_list), sep=" ")
