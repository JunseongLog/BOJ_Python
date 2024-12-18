#백준 1753번 최단경로 - 처음푸는 다익스트라 문제

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# 힙을 파이썬에서 구현
from queue import PriorityQueue

INF = int(1e12)

# 0. 입력 및 초기화
V, E = map(int, input().split()) #V정점, E간선선
start_node = int(input())
graph = [[] for _ in range(V+1)] # adj_list 인접 리스트
distance = [INF] * (V+1) # 각 정점까지의 거리리

# 1. 연결 정보 입력
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w]) # 리스트 형태로 넣어준다

# 2. Excute Dijkstra Algorithm
pq = PriorityQueue() # pq라는 이름의 힙을 구현
pq.put([0, start_node])
distance[start_node] = 0 # 시작점은 거리가 0

# 힙에 값이 없을 때까지 반복
while not pq.empty():
    # 힙에서 값을 꺼낸다
    cur_distance, cur_node = pq.get()

    for adj_node, adj_distance in graph[cur_node]:

        temp_distance = cur_distance + adj_distance

        if temp_distance < distance[adj_node]:

            distance[adj_node] = temp_distance
            pq.put([temp_distance, adj_node])

# Print result
for i in  range(1, V+1):
    if distance[i] == INF:
        print("INF")
        continue
    print(distance[i])