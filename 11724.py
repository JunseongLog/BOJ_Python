# 백준 11724번 연결 요소의 개수 DFS

import sys
# 재귀 횟수 늘려주기
sys.setrecursionlimit(10**6)
# 입력을 효율적으로 받기 위해 추가
input = sys.stdin.readline

def DFS(node):
    global graph, visited
    visited[node] = True

    for connect in range(1, N+1):
        if graph[node][connect] and not visited[connect]:
            DFS(connect)

# 0. 입력 및 초기화
N, M = map(int, input().split()) # 정점 N, 간선 M
graph = [[False] * (N + 1) for _ in range(N + 1)]
cnt = 0
visited = [False] * (N + 1)

# 1. 그래프 연결 요소
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

# 2. DFS호출
for node in range(1, N+1):
    # 방문되지 않은 노드라면 DFS
    if not visited[node]:
        DFS(node) # 한번 호출되면 i번과 연결된 것들은 모두 방문됨.
        cnt += 1

# 3. 출력
print(cnt)