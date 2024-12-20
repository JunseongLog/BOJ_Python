# 백준 숨바꼭질 3 연습

import sys
input = sys.stdin.readline

from queue import PriorityQueue

INF = int(1e12)
MAX = int(1e5)

N, K = map(int, input().split())
time = [INF] * (MAX+1)

pq = PriorityQueue()
pq.put([0, N]) # cur_time, start_node or position
time[N] = 0 # 시작점은 거리 0

while not pq.empty():

    cur_time, cur_position = pq.get()

    nexts = [
        [cur_time, cur_position * 2],
        [cur_time + 1, cur_position + 1],
        [cur_time + 1, cur_position - 1]
    ]

    for next_time, next_position in nexts:
        if 0 <= next_position <= MAX:
            if next_time < time[next_position]:
                time[next_position] = next_time
                pq.put([next_time, next_position])

print(time[K])