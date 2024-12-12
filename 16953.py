# 백준 16953번 A -> B

# 읽기 효율화
import sys
input = sys.stdin.readline

from collections import deque

def BFS(x, times):
    global matrix

    queue = deque()
    queue.append((x, times))

    while queue:
        x, times = queue.popleft()
        if x == B:
            print(times)
            return

        for nx in [x*2, int(str(x) + "1")]:
            if nx <= B:
                queue.append((nx, times + 1))
    print(-1) # B값에 도달하지 못하는 경우

# 0. 입력 및 초기화
A, B = map(int, input().split())

# 1. BFS호출
BFS(A, 1) # x좌표, 횟수
# 처음 값도 횟수로 카운트 하기 때문에 1을 넣어준다