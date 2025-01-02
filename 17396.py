# 백준 17396번 백도어

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

# Function Dijkstra
def Dijkstra(cur_time, start_node):
    
    time = [INF] * N

    pq = PriorityQueue()
    pq.put([cur_time, start_node]) # cur_time이 앞인 이유는 첫번째 값을 기준으로 우선순위 큐가 값을 꺼낸다
    time[start_node] = 0

    while not pq.empty():

        cur_time, cur_node = pq.get()

        if sight[cur_node]: # 시야가 1이면 그냥 넘겨준다
            continue
        
        # 문제 특성상 노드에서 다른 노드까지 한 경로에는 길이 하나라 없어도 되지만, 다익스트라를 구현할 때 그냥 추가하면 좋음
        if cur_time > time[cur_node]: # 어차피 갱신되지 않을 값도 넘겨준다
            continue

        for adj_node, adj_time in adj_list[cur_node]:
            temp_time = cur_time + adj_time
            if temp_time < time[adj_node]:
                time[adj_node] = temp_time
                pq.put([temp_time, adj_node])
    return time

# 0. Input & Initialization
N, M = map(int, input().split()) # N노드 M간선
INF = int(1e12)

sight = list(map(int, input().split()))

# 1. Create adj_list
adj_list = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    adj_list[a].append([b, t])
    adj_list[b].append([a, t])

# 2. Excute Dijkstra Algorithm
time_list = Dijkstra(0, 0) # cur_time, start_node

# 3. Print result
print(time_list[N-1] if time_list[N-1] != INF else -1)