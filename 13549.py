# 백준 13549번 숨바꼭질 3

# 읽기 속도 효율화
import sys
input = sys.stdin.readline

from collections import deque

# function BFS
def BFS(x, times):
    global visited

    queue = deque()
    queue.append((x, times))

    while queue:
        x, times = queue.popleft()

        if x == K:
            print(times)
            return
        
        for nx in [x*2, x-1, x+1]:
            if 0 <= nx <= MAX and not visited[nx]:
                if nx == (x*2):
                    visited[nx] = 1
                    queue.append((nx, times))
                else:
                    visited[nx] = 1
                    queue.append((nx, times+1))

# 0. 입력 및 초기화
N, K = map(int, input().split())

MAX = 100000
visited = [0] * (MAX+1)

# 1. BFS호출 및 출력력
BFS(N, 0)
