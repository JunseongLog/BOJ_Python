# 백준 13913번 숨바꼭질 4

# 읽는 속도 효율화
import sys
input = sys.stdin.readline

from collections import deque

#function BFS
def BFS(x, times, result_list):
    global visited

    queue = deque()
    queue.append((x, times, result_list))
    visited[x] = 1

    # N이 K보다 작을때 (N부터 K까지 1씩 빼면서 경로 출력)
    # 이걸 따로 처리 안해주면 계속 BFS를 돌리면서 경로를 찾아서 시간초과가 난다.
    if N > K:
        print(N-K) # 시간
        for i in range(N, K-1, -1):
            print(i, end=" ") # 경로
        return

    while queue:
        x, times, result_list = queue.popleft()
        if x == K:
            print(times)
            print(" ".join(map(str, result_list)))
            return

        for nx in [x*2, x-1, x+1]:
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = 1
                # append시키면 다른 갈래의 BFS의 result_list에도 append가 된다.
                # 그래서 원래 리스트에 값을 붙여주는 방식으로 매개변수를 넣는다.
                queue.append((nx, times+1, result_list + [nx]))

# 0. 입력 및 초기화
MAX = 100000
N, K = map(int, input().split())
visited = [0] * (MAX+1)

# 1. BFS호출
BFS(N, 0, [N]) #수빈 위치, 횟수, 경로
