# 백준 2644번 촌수계산

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(idx, cnt):
    global graph, visited, answer
    visited[idx] = True
    
    if idx == person2:
        answer = cnt
        return
    
    for i in graph[idx]:
        if not visited[i]:
            DFS(i, cnt + 1)

# 0. 입력 및 초기화
N = int(input())
person1, person2 = map(int, input().split())
M = int(input())
cnt = 0
# 못 찾으면 -1을 출력하기 위해 초기값 -1
# 만약 DFS에서 찾아지면 cnt 값을 answer에 입력
answer = -1

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 1. 연결 요소 입력
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

# 3. DFS호출
DFS(person1, 0)

# 4. 출력
print(answer)