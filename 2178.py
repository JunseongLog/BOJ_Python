# 백준 2178번 미로 탐색

import sys
input = sys.stdin.readline

from collections import deque

# 방향벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(y, x, distance):
    global visited

    queue = deque()
    queue.append((y, x, distance))
    visited[y][x] = True

    while queue:

        y, x, distance = queue.popleft()

        # 도착지점이면 거리 출력 & 리턴
        if y == N - 1 and x == M - 1:
            print(distance)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and game_map[ny][nx] and not visited[ny][nx]:
                queue.append((ny, nx, distance + 1))
                visited[ny][nx] = True
    # 도착지점에 도착을 못하면 -1 출력
    # 도착지점에 도착한다면 출력될 일이 없음
    print(-1)

# 0. 입력 및 초기화
N, M = map(int, input().split()) #N세로 M가로
game_map = []
visited = [[False] * (M) for _ in range(N)]

# 1. 연결 정보 입력
for i in range(N):
    game_map.append(list(map(int, input().rstrip())))

# 2. BFS호출 및 출력
BFS(0, 0, 1)