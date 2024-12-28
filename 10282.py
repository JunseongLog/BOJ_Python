# 백준 10282번 해킹

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

def Dijkstra(cur_time, start_node):

    time = [INF] * (n+1)

    pq = PriorityQueue()
    pq.put([cur_time, start_node])
    time[start_node] = 0

    while not pq.empty():

        cur_time, cur_node = pq.get()

        if cur_time > time[cur_node]: # 어차피 갱신되지 않을 값이 반복문을 돌지 않도록 방지
            continue

        for adj_node, adj_time in adj_list[cur_node]:
            temp_time = cur_time + adj_time
            if temp_time < time[adj_node]:
                time[adj_node] = temp_time
                pq.put([temp_time, adj_node])
    return time

# 0. 테스트 케이스 횟수
T = int(input())

for i in range(T):

    # 1. 입력 및 초기화
    n, d, start_node = map(int, input().split())
    INF = int(1e12)
    
    # 2. Create adj_list
    adj_list = [[] for _ in range(n+1)] # 노드 번호가 1부터터
    for i in range(d):
        a, b, s = map(int, input().split())
        adj_list[b].append([a, s])

    # 3. Excute Dijkstra Algorithm
    time_list = Dijkstra(0 , start_node) # cur_time, start_node

    # 4. Print result
    count = 0
    max_time = 0
    for i in range(1, n+1):
        if time_list[i] != INF:
            count += 1

        # 값이 INF면 방문할 수가 없는 곳이니까 걸러준다.
        if time_list[i] > max_time and time_list[i] != INF:
            max_time = time_list[i]
        
    
    print(count, end=" ")
    print(max_time)