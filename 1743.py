# 백준 1743 음식물 피하기

# 재귀 횟수, 읽는 속도 늘리기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(y, x):
    global visited, temp_count
    visited[y][x] = True

    temp_count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= M and 1 <= ny <= N and graph[ny][nx] and not visited[ny][nx]:
            DFS(ny, nx)

# 0. 입력 및 초기화
N, M, K = map(int, input().split()) #N세로 M가로
visited = [[False] * (M+1) for _ in range(N+1)]
graph = [[0] * (M+1) for _ in range(N+1)]
answer_list = [] # 넓이

# 1. 연결 요소 입력
for i in range(K):
    # 애초에 값이 (y, x)로 입력된다
    y, x = map(int, input().split())
    graph[y][x] = 1

# 2. DFS호출
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] and not visited[i][j]:
            temp_count = 0
            DFS(i, j)
            answer_list.append(temp_count)

# 3. 출력
if answer_list:
    print(max(answer_list))
else:
    print(0)