# 백준 2606번 BFS

import sys
input = sys.stdin.readline

from collections import deque

def BFS(idx):
    global visited, count


# 0. 입력 및 초기화
node_num = int(input())
edge_num = int(input())
# 컴퓨터 번호가 1번부터
graph = [[] for _ in range(node_num + 1)]
visited = [False] * (node_num + 1)
count = 0

# 1. 연결 정보 입력
for i in range(edge):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(X)

# 2. 오름차순 정리
for i in range(1, node_num + 1):
    graph[i].sort()

# 3. BFS호출
BFS(1)

# 4. 출력

