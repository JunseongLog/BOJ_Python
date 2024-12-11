# 백준 7576번 토마토

# 입력 효율화
import sys
input = sys.stdin.readline
# deque가 시간복잡도 측면에서 훨씬 효율적이라고 한다
from collections import deque

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# function BFS
def BFS():
    global queue, box

    while queue:

        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1 # 하루가 지날때마다 값을 1씩증가해서 넣는다
                queue.append((ny, nx))
                # 퍼져나갈 때마다 값을 증가시켜 주는 방식
                # 처음 익은 토마토는 1, 그 다음에 익으면 2, 3..4..

# 0. 입력 및 초기화
M, N = map(int, input().split()) #M가로 N세로
box = [] # 토마토 박스 리스트

queue = deque() # BFS호출 전에 큐에 값을 넣어줘야 해서 미리 선언

# 1. 연결정보 입력
for _ in range(N):
    box.append(list(map(int, input().split())))

# 2. 처음 사과 위치 큐에 기억 및 BFS호출
# 입력으로 들어왔을때의 익은 토마토의 위치를 저장
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
            # 이 값을 기준으로 퍼져나갈 거임

BFS()

# 3. 출력
for i in range(N):
    for j in range(M):
        if box[i][j] == 0: # 값이 0인게 하나라도 있으면 상하좌우로는 익힐 수가 없음
            print(-1)
            sys.exit(0) # 정상적인 프로그램 종료

# 모두 익었다면 가장 큰 값을 출력 -> 한번 나아갈때마다 1씩 증가해서 값을 넣어줬다
# 그래서 가장 큰 값에서 1을 빼면 그게 횟수가 된다
max_value = max(map(max, box))
print(max_value - 1)