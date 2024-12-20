# 백준 13549번 숨바꼭질 3

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

# 0. 입력 및 초기화
MAX = 100000
INF = int(1e12)

N, K = map(int, input().split())
graph = [0]
time = [INF] * (MAX + 1)

# 1. Excute Dijkstra Algorithm

pq = PriorityQueue()
pq.put([0, N]) # cur_time, start_node
time[N] = 0 # 시작점 거리값은 0

while not pq.empty():

    cur_time, cur_node = pq.get()

    nexts = [
        [cur_time, cur_node*2],
        [cur_time+1, cur_node+1],
        [cur_time+1, cur_node-1]
    ]
    for next_time, next_node in nexts:
        if 0 <= next_node <= MAX:
            if next_time < time[next_node]:
                time[next_node] = next_time
                pq.put([next_time, next_node])

# 2. Print result
print(time[K])