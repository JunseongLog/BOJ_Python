# 백준 1916번 최소비용 구하기

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

# 0. 입력 및 초기화
INF = int(1e12)
N = int(input())
M = int(input())

# 1. Create adj_list
adj_list = [ [] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c]) # adj_node, adj_cost

start_node, end_node = map(int, input().split())

# 시작점과 도착점이 같은 경우 처리리
if start_node == end_node:
    print(0)
    sys.exit(0)

# 2. Excute Dijkstra Algorithm
cost = [INF] * (N+1)

pq = PriorityQueue()
pq.put([0, start_node]) # cur_cost, cur_node
cost[start_node] = 0

while not pq.empty():

    cur_cost, cur_node = pq.get()

    # 이미 더 작은 값으로 처리된 노드가 의미없이 반복문을 돌지 않도록 방지(최적화화)
    if cost[cur_node] < cur_cost:
        continue
    # 이 조건은 같은 경로에 간선이 여러개 있을때 유효함.
    # 간선이 중복되지 않거나 각 노드쌍마다 유일한 경로만 있을 때는 필요 없음.

    for adj_node, adj_cost in adj_list[cur_node]:

        temp_cost = cur_cost + adj_cost

        if temp_cost < cost[adj_node]:
            cost[adj_node] = temp_cost
            pq.put([temp_cost, adj_node])

# 3. Print result
print(cost[end_node])