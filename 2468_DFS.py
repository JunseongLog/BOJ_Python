# 백준 2468번 안전 영역

# 재귀 횟수, 읽는 속도 늘리기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(y, x):
    global visited
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] > hight and not visited[ny][nx]:
            DFS(ny, nx)

# 0. 입력 및 초기화
N = int(input())
graph = []
count_list = [] # 카운트를 모두 넣어주고 가장 큰 값을 출력할 리스트

# 1. 연결 정보 입력
for i in range(N):
    graph.append(list(map(int, input().split())))

# 2. 전체 반복
times = 0
times = max(map(max, graph))
# times는 이차원 리스트에서 가장 큰값
# 0부터 times - 1까지 반복문 돌리면 될듯

# hight는 빗물 높이 (0부터 times-1까지 반복)
for hight in range(times):
    # 여기서 visited를 선언해야 높이가 바뀔때마다 초기화 됨
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > hight and not visited[i][j]:
                DFS(i, j)
                count += 1
    
    count_list.append(count)

# 3. 출력
print(max(count_list))