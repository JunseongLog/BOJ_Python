# 백준 11725번 트리의 부모 찾기

def DFS(idx):
    global graph, visited, answer
    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]:
            # DFS는 부모노드에서 자식노드로 탐색을 한다
            # 그러므로 호출된 idx값이 부모노드의 숫자이다
            answer[i] = idx
            DFS(i)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 0. 입력 및 초기화
N = int(input())
graph = [[]for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)

# 1. 연결 요소 입력
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

# 3. DFS호출
DFS(1) #idx

# 4. 출력
for i in range(2, N+1):
    print(answer[i])