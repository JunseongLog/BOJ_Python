# 백준 1238번 파티 풀이 2

# 1번부터 N번까지에서 X로 가는 다익스트라를 N번이나 하기 부담스럽다면
# graph를 완전히 뒤집어서 X에서 시작하는 다익스트라를 돌리면 한번에 해결할 수 있다.

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

# Dijkstra Algorithm
def Dijkstra(start_node, list):
    
    distance = [INF] * (N+1)

    pq = PriorityQueue()
    pq.put([0, start_node]) # cur_distance, cur_node
    distance[start_node] = 0 
    
    while not pq.empty():

        cur_distance, cur_node = pq.get()

        for adj_node, adj_distance in list[cur_node]:
            # 다음 노드까지의 거리를 합친 값
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

# 1. Create adj_list & reverse adj_list
adj_list = [ [] for _ in range(N+1)]
adj_list_reverse = [ [] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])
    adj_list_reverse[b].append([a, c])

# 2. Excute Dijkstra Algorithm
distance_to_X = Dijkstra(X, adj_list_reverse)
distance_to_everynode = Dijkstra(X, adj_list)

# 3. Print result
result = []
for i in range(1, N+1):
    result.append(distance_to_X[i] + distance_to_everynode[i])

max_value = max(result)
print(max_value)