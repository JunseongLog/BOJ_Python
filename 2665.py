# 백준 2665번 미로만들기

# 읽는 속도 효율화화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

# 방향벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Function Dijkstra
def Dijkstra(cur_count, y, x):

    count = [[INF] * N for _ in range(N)]

    pq = PriorityQueue()
    pq.put([cur_count, y, x])
    count[y][x] = 0 # 어차피 시작점은 흰방이다

    while not pq.empty():

        cur_count, y, x = pq.get()

        if cur_count > count[y][x]: # 불필요한 값 방지
            continue
        
        # 다익스트라 + 시뮬레이션일때 다음 스텝 옮기는 방식
        # 인접 리스트라면 for adj_count, adj_node in adj_list[cur_node]: 방식으로 사용용
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:

                # 현재 값보다 최소여서 갱신해야 한다면
                if cur_count + adj_matrix[ny][nx] < count[ny][nx]:
                    temp_count = cur_count + adj_matrix[ny][nx]
                    count[ny][nx] = temp_count
                    pq.put([temp_count, ny, nx])
    return count

# 0. 입력 및 초기화
INF = int(1e12)
N = int(input())

# 1. 연결 정보 입력
actual_map = []
for i in range(N):
    actual_map.append(list(map(int, input().rstrip())))

# 갯수를 카운트 해야하는 건 검은 방인데 검은 방이 0이라서 이대로 사용하면 불편하다
# 그래서 흰방을 0 검은 방을 1으로 바꾼 값을 adj_matrix에 넣어준다다
# adj_matrix 실제로 사용할 인접 행렬
adj_matrix = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if actual_map[i][j] == 0: # 검은 방이면
             adj_matrix[i][j] = 1

# 2. Excute Dijkstra Algorithm
count_list = Dijkstra(0, 0, 0) # cur_count, y, x

# 3. Print result
print(count_list[N-1][N-1])