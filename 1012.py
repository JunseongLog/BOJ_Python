# 백준 1012번 유기농 배추 DFS

# 백준에는 재귀가 1000으로 제한되기 때문에 늘려준다 
import sys
sys.setrecursionlimit(10**6)

# 방향 벡터 동-서-남-북 순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(i, j):
    global graph
    graph[i][j] = False

    # 방향벡터로 4방향을 탐색
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]

        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx]:
            DFS(ny, nx)



T = int(input())

for _ in range(T):
    # 0. 입력 및 초기화

    # 가로 M, 세로N, 배추 개수 K
    M, N, K = map(int, input().split())
    graph = [[False] * M for _ in range(N)]
    cnt = 0

    # 1. 그래프 연결 값 넣기
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = True

    # 2. DFS 호출

    for i in range(N):
        for j in range(M):
            if graph[i][j] == True:
                DFS(i, j)
                cnt += 1
    
    # 3. 출력
    print(cnt)

    


    
