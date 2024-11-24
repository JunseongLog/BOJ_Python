# 백준 4963번 섬의 개수

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(y, x):
    global world_map
    world_map[y][x] = 0

    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < w and 0 <= new_y < h and world_map[new_y][new_x]:
            DFS(new_y, new_x)

# 뱡향벡터 정의 12시방향부터 시계방향[8가지]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 반복문에 들어가기 위해 초기값 할당
w, h = 1, 1

while w != 0 and h != 0:


    # 0. 입력 및 초기화
    w, h = map(int, input().split()) #너비w 높이h

    if w == 0 and h == 0:
        break

    world_map = []
    cnt = 0

    # 1. 연결 요소 입력
    for i in range(h):
        world_map.append(list(map(int, input().split())))
    
    # 2. DFS 호출
    for i in range(h):
        for j in range(w):
            if world_map[i][j]:
                DFS(i, j)
                # 메인에서 한번 호출되면 섬하나로 카운트
                cnt += 1
    

    # 3. 출력
    print(cnt)