# 1260번 DFS와 BFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

def DFS(idx):
    global graph, answer_dfs, visited
    visited[idx] = True
    # 인덱스 순서대로 추가
    answer_dfs.append(idx)

    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            DFS(i)

def BFS(idx):
    global graph, answer_bfs, visited

    queue = deque()
    queue.append(idx)
    visited[idx] = True

    while queue:

        number = queue.popleft()
        answer_bfs.append(number)

        for i in range(N+1):
            if not visited[i] and graph[number][i]:
                visited[i] = True
                queue.append(i)
        


# 0. 입력 및 초기화
N, M, V = map(int, input().split())
visited = [False] * (N+1)
answer_dfs = []
answer_bfs = []

# 1. 연결 정보 입력
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# 2. DFS/BFS 호출
DFS(V) #idx

# BFS에서 사용하기 위해 다시 False로 초기화
for i in range(N+1):
    visited[i] = False

BFS(V)

# 3. 출력

# '중간에 넣을 값'.join(string)이다. 이거 문자열 기준이므로
# map함수로 문자열로 만들어준다.
print(' '.join(map(str, answer_dfs)))
print(' '.join(map(str, answer_bfs)))
