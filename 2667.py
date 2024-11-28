# 백준 2667번 단지번호붙이기

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(y, x):
    global maps, visited, count
    visited[y][x] = True
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and maps[ny][nx] and not visited[ny][nx]:
            DFS(ny, nx)

# 0. 입력 및 초기화
N = int(input())
maps = []
visited = [[False] * N for _ in range(N)]

cnt_lst = []
answer = 0

# 1. 연결 요소 입력
for i in range(N):
    maps.append(list(map(int, input().rstrip())))

# 2. DFS 호출
for i in range(N):
    for j in range(N):
        if maps[i][j] and not visited[i][j]:
            count = 0
            DFS(i, j)
            cnt_lst.append(count)

            answer += 1

# 3. 오름차순 정리
cnt_lst.sort()

# 4. 출력
print(answer)
for i in range(len(cnt_lst)):
    print(cnt_lst[i])
