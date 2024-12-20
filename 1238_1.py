# 백준 1238번 풀이 1
# 풀이가 두 가지 방법이 가능해서 2가지로 소스파일을 따로 만든다.
# 1번부터 N번까지 다익스트라 + x에서 각 번호 까지 다익스트라
# 총 N+1번 다익스트라를 돌리는 풀이이 


# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

def Dijkstra(start_node):
    global distance_list

    distance = [INF] * (N+1)

    pq = PriorityQueue()
    pq.put([0, start_node])
    distance[start_node] = 0

    while not pq.empty():

        cur_distance, cur_node = pq.get()

        for adj_node, adj_distance in adj_list[cur_node]:
            temp_distance = cur_distance + adj_distance
            if temp_distance < distance[adj_node]:
                distance[adj_node] = temp_distance
                pq.put([temp_distance, adj_node])
    
    return distance

# 0. 입력 및 초기화
INF = int(1e12)
N, M, X = map(int, input().split()) 
# N: 마을(노드)의 수
# M: 단방향 간선의 갯수
# X: 파티를 여는 마을(노드)

adj_list = [[] for _ in range(N+1)]
distance_to_X = [] # Dijkstra from i to X
distance_X = [] # Dijkstra to Everynode

# Create adj_list
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])

# Dijkstra from i to X
for i in range(1, N+1):
    distance = Dijkstra(i)
    distance_to_X.append(distance[X])

# Dijkstra from X to Everynode
distance_X = Dijkstra(X)

result = []

for i in range(1, N+1):
    result.append(distance_to_X[i - 1] + distance_X[i])


max_value = max(result)
print(max_value)