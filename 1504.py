# 백준 1504번 특정한 최단 경로

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# 힙 모듈 import
from queue import PriorityQueue

# function Dijkstra
# 여러번 다익스트라 알고리즘을 이용할 거라서 함수로 구현현
def Dijkstra(start_node):

    distance = [INF] * (N+1)

    pq = PriorityQueue()
    pq.put([0, start_node])
    distance[start_node] = 0

    while not pq.empty():
        cur_distance, cur_node = pq.get()
        
        for adj_node, adj_distance in graph[cur_node]:
            temp_distance = cur_distance + adj_distance
            if temp_distance < distance[adj_node]:
                distance[adj_node] = temp_distance
                pq.put([temp_distance, adj_node])

    return distance

# distance 초기값으로 넣어줄 INF 선언언
INF = int(1e12)

# 0. 입력 및 초기화
N, E = map(int, input().split()) #N노드 E엣지
graph = [[] for _ in range(N+1)]


# 1. 연결 정보 입력
for _ in range(E):
    a, b, c = map(int, input().split())
    # 양방향 그래프
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

distance_1 = Dijkstra(1) # 1번 노드를 시작점으로 거리값
distance_v1 = Dijkstra(v1) # v1 노드를 시작점으로 거리값
distance_v2 = Dijkstra(v2) # v2 노드를 시작점으로 거리값

# CASE1:  1 -> v1 -> v2 -> N
# CASE2:  1 -> v2 -> v1 -> N 
case1 = distance_1[v1] + distance_v1[v2] + distance_v2[N]
case2 = distance_1[v2] + distance_v2[v1] + distance_v1[N]

# Print result
min_value = min(case1, case2)
print(min_value if min_value < INF else -1)