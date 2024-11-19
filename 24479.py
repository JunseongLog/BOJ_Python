# 백준 24479번 알고리즘 수업 - 깊이 우선 탐색 1

def DFS(idx):
    global visited, graph, answer, order

    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            DFS(i)

# 재귀 횟수 and 읽기 속도 늘리기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 0. 입력 및 초기화

# N 정점, M 간선, R 시작지점
N, M, R = map(int, input().split())
graph = [ [] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1) # 탐색 안한 것은 0이여야 함
order = 1

# 1. 연결 요소 입력
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()
# 배열을 쓴다면 알아서 오름차순으로 탐색 가능 하지만 노드 갯수 제한이 크면 배열을 못씀
# graph가 더 효율적임. 딱 쓰는 메모리만 사용하는 방식. 대신 오름차순으로 정렬해줘야 한다

# 3. DFS호출
DFS(R) #idx R과 연결된 모든 요소만 탐색하는 거라서 반복문은 없음

# 4. 출력
for i in range(1, N+1):
    print(answer[i])