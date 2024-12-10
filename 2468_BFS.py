# 백준 2468번 안전 영역 BFS풀이

# 입력 속도 늘리기
import sys
input = sys.stdin.readline

# deque import
from collections import deque

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def BFS(y, x):
    global visited, count

    queue = deque()
    queue.append((y, x))
    visited[y][x] =  True

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] > rain_hight and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
                
# 0. 입력 및 초기화
N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]
result = 1

# 1. 연결 정보 입력
for i in range(N):
    graph.append(list(map(int, input().split())))

# 2. BFS호출
max_value = max(map(max, graph)) # 그래프에서 가장 큰 값 구하기
# 가장 큰 높이 값의 -1 만큼 높이까지 돌리면 될듯
for rain_hight in range(max_value):
    visited = [[False] * N for _ in range(N)] # 방문 배열 초기화
    count = 0 # 카운트 초기화

    for i in range(N):
        for j in range(N):
            if graph[i][j] > rain_hight and not visited[i][j]:
                BFS(i, j)
                count += 1

    if result < count:
        result = count

# 3. 출력
print(result)