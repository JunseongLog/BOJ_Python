# 백준 24480번 알고리즘 수업 - 깊이 우선 탐색 2
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(idx):
    global graph, visited, answer, order

    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            DFS(i)

# 0. 입력 및 초기화
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)
order = 1

# 1. 연결 요소 입력
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. 내림차순 정렬
for i in range(1, N+1):
    graph[i].sort(reverse=True)

# 3. DFS호출
DFS(R) #idx

# 4. 출력
for i in range(1, N+1):
    print(answer[i])