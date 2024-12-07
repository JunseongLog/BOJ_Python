# 백준 2606번 BFS

import sys
input = sys.stdin.readline

from collections import deque

def BFS(idx):
    global visited, count
    queue = deque()

    # BFS는 처음 값은 직접 넣어줘야 함
    queue.append(idx)
    visited[idx] = True

    while queue:

        number = queue.popleft()

        for value in graph[number]:
            if not visited[value]:
                # BFS는 큐에 값을 넣으면서 방문 처리
                queue.append(value)
                visited[value] = True
                count += 1
                

# 0. 입력 및 초기화
node_num = int(input())
edge_num = int(input())
# 컴퓨터 번호가 1번부터
graph = [[] for _ in range(node_num + 1)]
visited = [False] * (node_num + 1)
count = 0

# 1. 연결 정보 입력
for i in range(edge_num):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. 오름차순 정리
for i in range(1, node_num + 1):
    graph[i].sort()

# 3. BFS호출
BFS(1)

# 4. 출력
print(count)