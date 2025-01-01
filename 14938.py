# 백준 14938번 서강그라운드

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

# Function Dijkstra Algorithm
def Dijkstra(cur_distance, start_node):
    global result, distance

    pq = PriorityQueue()
    pq.put([cur_distance, start_node])
    distance[start_node] = 0 # 첫 노드 거리 0

    while not pq.empty():

        cur_distance, cur_node = pq.get()
        
        # 어차피 갱신되지 않은 값은 넘겨준다
        if cur_distance > distance[cur_node]:
            continue 

        for adj_node, adj_distance in adj_list[cur_node]:

            temp_distance = cur_distance + adj_distance

            if temp_distance < distance[adj_node]:
                distance[adj_node] = temp_distance
                pq.put([temp_distance, adj_node])

    return
    
# 0. 입력 및 초기화
# N 노드 갯수, M 수색범위, R 간선 갯수
N, M, R = map(int, input().split())
INF = int(1e12)

item_number = list(map(int, input().split()))

# 1. Create adj_list
adj_list = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, t = map(int, input().split())
    adj_list[a].append([b, t])
    adj_list[b].append([a, t])

# 2. Excute Dijkstra Algorithm & Print result
result = 0
for i in range(1, N+1):
    distance = [INF] * (N+1)
    Dijkstra(0, i)
    sum = 0

    for j in range(1, N+1):
        if distance[j] <= M:
            sum += item_number[j-1]
    
    result = max(result, sum)

print(result)