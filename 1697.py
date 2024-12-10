# 백준 1697번 숨바꼭질

import sys
input = sys.stdin.readline

from collections import deque

def BFS(x):
    global visited
    time = 0
    queue = deque()
    queue.append((x, time))

    while queue:
        x, time = queue.popleft()
        if x == K:
            print(time)
            return

        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx < 100000 + 1 and not visited[nx]:
                queue.append((nx, time + 1))
                visited[nx] = True


# 0. 입력 및 초기화

# N:수빈 위치, M:동생 위치
N, K = map(int, input().split())
visited = [False] * (100000 + 1) # 맵이자 방문여부 확인 리스트

# 1. BFS호출 및 출력
BFS(N)