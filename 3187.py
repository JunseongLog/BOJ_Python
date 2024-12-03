# 백준 3187번 양

# 떠오른 풀이
"""
 늑대나 양, 빈 공간을 발견하면 메인에서 DFS호출
 상하좌우를 살피면서 방문하지 않았고, #이 아니면 재호출.
 한번의 메인 호출이 끝나면 양과 늑대 수를 비교해서 다른 값에 넣어주고
 원래 늑대와 양을 카운트했던 변수는 0으로 초기화
"""

# 재귀 횟수, 읽는 속도 늘리기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(y, x, type):
    global visited, backyard, wolf_cnt, sheep_cnt
    visited[y][x] = True

    # 카운트
    if type == "v":
        wolf_cnt += 1
    elif type == "k":
        sheep_cnt += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and backyard[ny][nx] in permission and not visited[ny][nx]:
            DFS(ny, nx, backyard[ny][nx])

# 0. 입력 및 초기화
R, C = map(int, input().split()) #R세로 C가로
visited = [[False] * C for _ in range(R)]
backyard = []
living_wolf = 0
living_sheep = 0

# 메인에서 DFS호출할때 "#"제외 나머지는 통과
permission = [".", "v", "k"]

# 1. 연결 정보 입력
for i in range(R):
    backyard.append(list(input().rstrip()))
# 이중 리스트로 만들어야하기 때문에 list함수를 사용

# 2. DFS호출
for i in range(R):
    for j in range(C):
        if backyard[i][j] in permission and not visited[i][j]:
            wolf_cnt = 0
            sheep_cnt = 0
            DFS(i, j, backyard[i][j])

            # 늑대보다 양이 더 많으면 양 카운트
            if sheep_cnt > wolf_cnt:
                living_sheep += sheep_cnt
            else: # 그 외에는 늑대만 카운트
                living_wolf += wolf_cnt
            

# 3. 출력
print(living_sheep, living_wolf)