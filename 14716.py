# 백준 14716번 현수막

# 재귀 횟수, 읽는 속도 늘리기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 위부터 시계방향순
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def DFS(y, x):
    global graph
    graph[y][x] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and graph[ny][nx]:
            DFS(ny, nx)

# 0. 입력 및 초기화
M, N = map(int, input().split()) #M세로 N가로
graph = []
cnt = 0

# 1. 연결 정보 입력
for i in range(M):
    graph.append(list(map(int, input().split())))
    
# 2. DFS호출
for i in range(M):
    for j in range(N):
        if graph[i][j]:
            DFS(i, j)
            cnt += 1

# 3. 출력
print(cnt)