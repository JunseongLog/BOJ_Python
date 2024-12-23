# 백준 4485번 녹색 옷 입은 애가 젤다지?

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import PriorityQueue
from queue import PriorityQueue

# 방향 벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Function Dijkstra Algorithm
def Dijkstra(cur_count, y, x):

    count = [ [INF] * N for _ in range(N)]

    pq = PriorityQueue()
    pq.put([cur_count, y, x]) # 인접 리스트라면 cur_distance, cur_node
    count[y][x] = cur_count # 시작 좌표 값 0

    while not pq.empty():

        cur_count, y, x = pq.get()

        # 인접 행렬 + 시뮬레이션이면 아래 조건문까지가 for adj_node, adj_distance in adj_list[cur_node]를 대신함
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:

                # 원래 있는 값보다 갱신할 값이 더 작으면 갱신
                if cur_count + adj_matrix[ny][nx] < count[ny][nx]:
                    
                    temp_count = cur_count + adj_matrix[ny][nx]
                    count[ny][nx] = temp_count
                    pq.put([temp_count, ny, nx])

    return count

# 0. 전체 반복
INF = int(1e12)
num_count = 0

while True:

    # 1. 입력 및 초기화
    N = int(input())
    num_count += 1

    if N == 0: # 종료 조건
        break

    # 2. Create adj_matrix
    adj_matrix = []
    
    for i in range(N):
        adj_matrix.append(list(map(int, input().split())))

    # 3. Excute Dijlstra Algorithm
    result = Dijkstra(adj_matrix[0][0], 0, 0) # cur_count, 시작 좌표값(0, 0)

    # 4. Print result
    print(f"Problem {num_count}: {result[N-1][N-1]}")