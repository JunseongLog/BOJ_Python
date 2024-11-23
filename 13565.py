# 13565번 침투

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(y, x):
    global graph, visited, result
    visited[y][x] = True

    if y == (M - 1):
        result = "YES"

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < M and not visited[new_y][new_x] and not graph[new_y][new_x]:
            DFS(new_y, new_x)

    
# 방향벡터 동-서-남-북 순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 0. 입력 및 초기화
M, N = map(int, input().split()) #M세로 N가로
graph = []
visited = [[False] * N for _ in range(M)]
# 결과값을 담는 변수
result = "NO"

# 1. 연결 요소 입력
for i in range(M):
    # rstrip으로 오른쪽 공백을 삭제
    graph.append(list(map(int, input().rstrip())))

# 2. DFS호출
for i in range(N):
    if not visited[0][i] and not graph[0][i]:
        DFS(0, i) #idx

# 3. 출력
print(result)