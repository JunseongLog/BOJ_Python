# 백준 1261번 알고스팟

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

# Import deque
from queue import PriorityQueue

# 방향 벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS functions
def Dijkstra(cur_count ,y, x):
    
    count = [[INF] * M for _ in range(N)] # 각 좌표까지 최소 몇개의 벽 부수기가 필요한지 저장할 리스트

    pq = PriorityQueue()
    pq.put([cur_count, y, x])
    count[y][x] = 0 # 시작 값은 0

    while not pq.empty():

        cur_count, y, x = pq.get() # 원래라면 cur_distance, cur_node인데 인접 행렬이라서 y, x값이다

        # 이미 갱신한 값인데 그 값보다 크면 갱신할 필요가 없음. 
        #아래로 내려가도 갱신은 안되겠지만 불필요하게 반복문 실행을 줄이기 위해해
        if cur_count > count[y][x]: 
            continue
        
        # 인접 리스트면 바로 밑의 if문까지가 for adj_node, adj_distance in adj_list[cur_node]로 표현이 된다.
        # 인접 행렬이면 이렇게 사용해야함.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N: # 유효 범위 내라면
                
                # 현재 최솟값보다 작으면
                if cur_count + adj_matrix[ny][nx] < count[ny][nx]: # 원래라면 cur_distance + adj_distance 인데 인접 행렬이고, 가중치가 리스트 값이라서
            
                    temp_count = cur_count + adj_matrix[ny][nx]   
                    count[ny][nx] = temp_count
                    pq.put([temp_count, ny, nx])
    
    return count

# 0. 입력 및 초기화
INF = int(1e12)
M, N = map(int, input().split()) # M가로 N세로

# 1. Create adj_matrix
adj_matrix = []
for _ in range(N):
    # 공백으로 구분되어 들어올땐 input().split()
    # 공백없이 입력될 땐 input().rstrip()
    adj_matrix.append(list(map(int, input().rstrip())))

# 2. Excute BFS function
count_list = Dijkstra(0, 0, 0) # 현재거리, 시작 좌표값(0, 0)

# 3. Print result
print(count_list[N-1][M-1])