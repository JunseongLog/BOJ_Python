# 백준 2606번 바이러스 DFS

def DFS(idx):
    global graph, visited, answer
    visited[idx] = True
    answer += 1

    for i in range(N + 1):
        if not visited[i] and graph[idx][i]:
            DFS(i)

# 0. 입력 및 초기화
N = int(input())
M = int(input())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

# 1. graph 연결 값 넣기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True


# 2. DFS 호출
DFS(1)

# 3. 출력
print(answer - 1)
    
