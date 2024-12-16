# 백준 12851번 숨바꼭질 2

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# 큐 모듈 import
from collections import deque

def BFS(x, times):
    global visited, min_time, count

    queue = deque()
    queue.append((x, times))
    visited[x] = 0 #방문처리

    while queue:
        x, times = queue.popleft()

       # 위치 값이 동생위치에 도달한다면
        if x == K:
            count += 1
            min_time = visited[x]
            
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= MAX and (visited[nx] == -1 or visited[nx] == times + 1):
                visited[nx] = times +1 #방문처리: 최소거리(시간)을 기록
                queue.append((nx, times+1))

# 0. 입력 및 초기화
MAX = 100000

N, K = map(int, input().split()) # N수빈 K동생
visited = [-1] * (MAX+1)

min_time = 0 # 최단 시간 저장
count = 0 # 최단 시간 경로 카운트

# 1. BFS호출
BFS(N, 0)

# 2. 출력
print(min_time)
print(count)