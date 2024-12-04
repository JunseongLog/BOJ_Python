# 백준 1325번 효율적인 해킹
# 시간초과, 메모리초과 코드 - 일반적인 DFS로는 통과되지 않는 것 같다
# BFS를 사용해야 할듯

# 재귀 횟수, 읽는 속도 늘리기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(idx):
    global visited, graph, temp_count
    visited[idx] = True
    temp_count += 1

    for number in graph[idx]:
        if not visited[number]:
            DFS(number)

# 0. 입력 및 초기화
N, M = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

count_list = [0] * (N+1)

# 1. 연결 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a) # 단방향 그래프

# 2. DFS호출
for i in range(1, N+1):
    visited = [False] * (N+1) # 매번수 마다 방문 여부도 초기화
    temp_count = 0 # 캄퓨터 마다 갯수를 세어준다
    DFS(i) # idx
    count_list[i] = temp_count # 각 번호에 맞게 값을 대입

# 3. 출력
max_value = max(count_list) # 최대값을 뽑는다

for i in range(1, N+1):
    # 최댓값과 같은 인덱스 출력
    if count_list[i] == max_value:
        print(i, end=" ")