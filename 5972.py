# 백준 5972번 택배 배송

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

# Function Dijkstra
def Dijkstra(cur_cost, start_node):

    cost = [INF] * (N+1)

    pq = PriorityQueue()
    pq.put([cur_cost, start_node])
    cost[start_node] = 0

    while not pq.empty():

        cur_cost, cur_node = pq.get()

        if cur_cost > cost[cur_node]:
            continue

        for adj_node, adj_cost in adj_list[cur_node]:
            temp_cost = cur_cost + adj_cost

            if temp_cost < cost[adj_node]:
                cost[adj_node] = temp_cost
                pq.put([temp_cost, adj_node])
    return cost

# 0. 입력 및 초기화
INF = int(1e12)
N, M = map(int, input().split()) # N 노드 갯수, M 간선 갯수

# 1. Create adj_list
adj_list = [ [] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    adj_list[a].append([b, t])
    adj_list[b].append([a, t])

# 2. Excute Dijkstra Algorithm
cost_list = Dijkstra(0, 1) # cur_cost, start_node

# 3. Print result
print(cost_list[N])