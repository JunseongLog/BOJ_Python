# 백준 2583번 영역 구하기

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(y, x):
    global visited, answer, temp_count
    # 방문처리
    visited[y][x] = True
    # 갯수 카운트
    temp_count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] and not visited[ny][nx]:
            DFS(ny, nx)

# 0. 입력 및 초기화
M, N, K = map(int, input().split()) #M세로 N가로 K사각형 갯수
visited = [[False] * N for _ in range(M)]
answer = []
count = 0

# 1. 연결 정보 입력
graph = [[1] * N for _ in range(M)]
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0

# 2. DFS호출
for i in range(M):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            temp_count = 0
            DFS(i, j)
            answer.append(temp_count)
            count += 1

# 3. 구한 넓이 오름차순 정리
answer.sort()

# 4. 출력
print(count)
# join함수는 문자열 리스트형태만 넣어줘야 해서 형변환
print(" ".join(map(str, answer)))