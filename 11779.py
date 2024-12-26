# 백준 11779번 최소비용 구하기 2

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

# Import defaultdict
from collections import defaultdict

# Function Dijkstra
def Dijkstra(cur_cost, start_node):
    global cost, parents

    # parents 배열 초기화
    for i in range(1, N+1):
        parents[i] = None

    pq = PriorityQueue()
    pq.put([cur_cost, start_node])
    cost[start_node] = 0 # 시작점 비용 0

    while not pq.empty():

        cur_cost, cur_node = pq.get()

        # 어차피 갱신이 안될 값이 무의미한 반복문을 피하기 위해
        if cur_cost > cost[cur_node]:
            continue

        for adj_node, adj_cost in adj_list[cur_node]:
            
            temp_cost = cur_cost + adj_cost
            # 갱신 조건이고 아래가 갱신 할 값, 갱신할떄 부모노드를 넣어준다.
            if temp_cost < cost[adj_node]:
                cost[adj_node] = temp_cost
                pq.put([temp_cost, adj_node])
                parents[adj_node] = cur_node # 자식노드 키에 값은 부모 노드

    # 경로 역추적
    route = [] # 경로를 넣을 리스트

    now = end_node 
    while now != start_node:
        route.append(now) # 값을 넣고 이전 경로를 now에 넣는다
        now = parents[now]
    route.append(start_node)

    # 역추적이므로 route에 반대로 들어갔기 때문에 역으로 정렬
    route.reverse()
    return route
    
# 0. 입력 및 초기화
INF = int(1e12)

N = int(input())
M = int(input())
cost = [INF] * (N+1)

# 1. Create adj_list
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    adj_list[a].append([b, t])

start_node, end_node = map(int, input().split())

# 경로를 역추적할 딕셔너리리
parents = defaultdict()

# 2. Excute Dijkstra
route = Dijkstra(0, start_node) # cur_cost, start_node

# 3. Print result
print(cost[end_node])
print(len(route))
print(" ".join(map(str, route)))