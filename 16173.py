# 백준 16173번 점프왕 쩰리(Small)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 동-남 순
dx = [1, 0]
dy = [0, 1]

def DFS(y, x):
    global game_map, answer, visited

    visited[y][x] = True
    
    if y == (N-1) and x == (N-1):
        answer = "HaruHaru"
        return

    # 점프를 지그제그로 하지 못함 한방향으로만 가능
    # 만약 점프가 지그제그로 됐으면 훨씬 까다로웠을 거임
    for i in range(2):
        new_x = x + dx[i] * game_map[y][x]
        new_y = y + dy[i] * game_map[y][x]
        if 0 <= new_x < N and 0 <= new_y < N and not visited[new_y][new_x]:
            DFS(new_y, new_x)
        

# 0. 입력 및 초기화
N = int(input())
game_map = []
answer = "Hing"
visited = [[False] * N for _ in range(N)]

# 1. 게임맵 정보 입력
for _ in range(N):
    game_map.append(list(map(int, input().split())))

# 2. DFS호출
DFS(0, 0) # y, x

# 3. 출력
print(answer)