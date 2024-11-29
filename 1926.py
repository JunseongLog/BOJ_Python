# 백준 1926번 그림

# 재귀 횟수, 읽는 속도 늘리기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(y, x):
    global visited, temp_count
    visited[y][x] = True

    temp_count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] and not visited[ny][nx]:
            DFS(ny, nx)


# 0. 입력 및 초기화
N, M = map(int, input().split()) #N세로 M가로
visited = [[False] * M for _ in range(N)]
graph = []
count = 0 # 그림 갯수
answer_list = [] # 넓이

# 1. 연결 요소 입력
for i in range(N):
    graph.append(list(map(int, input().split())))


# 2. DFS호출
for i in range(N):
    for j in range(M):
        if graph[i][j] and not visited[i][j]:
            temp_count = 0
            DFS(i, j)
            count +=1
            answer_list.append(temp_count)

# 3. 출력
print(count)

# 그래프가 다 0이여서 answer_list에 값이 없으면
# max함수가 참조값이 없어서 valueerror가 발생. 예외처리해줘야함
if answer_list:
    print(max(answer_list))
else:
    print(0)