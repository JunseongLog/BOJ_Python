# 백준 17086번 아기 상어 2

# visited에 상어에서 부터 거리 값을 넣어준다.
# 만약 현재 들어갈 거리 값이 기존 거리값보다 작으면 덮어씌운다.
# 가장 가까운 상어를 기준으로 안전거리를 측정하기 때문에에

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# deque
from collections import deque

# 방향 벡터 12시부터 시계방향
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    
# 0. 입력 및 초기화
N, M = map(int, input().split()) #N세로 M가로
space = []
visited = [[0] * M for _ in range(N)]

# 1. 연결 정보 입력
for _ in range(N):
    space.append(list(map(int, input().split())))

# 2. BFS구현 및 호출
queue = deque()

# BFS이기 때문에 상어가 있는 위치를 큐에 넣어주면 가까운 거리부터 visited에 값이 들어간다.
# 먼저 도착한 값이 가장 가까운 상어에서부터 도착한 것이기 때문에 따로 살펴볼 필요없이 각칸에 맞는 값이 들어간다.
for i in range(N):
    for j in range(M):
        if space[i][j] and visited[i][j] == 0:
            visited[i][j] = -1 #상어 자리는 -1로 설정
            queue.append((i, j, 0))

while queue:

    y, x, distance = queue.popleft()

    # 8가지 인접 방향 탐색
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내이고, 값이 0이면서 visited 값이 0일때 큐에 추가가
        if 0 <= nx < M and 0 <= ny < N and space[ny][nx] == 0 and visited[ny][nx] == 0:
            visited[ny][nx] = distance + 1
            queue.append((ny, nx, distance+1))
# 3. 출력
max_value = max(map(max, visited)) # 이차원 리스트에서 가장 큰 값 구하기
print(max_value)