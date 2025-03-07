# 백준 3085번 사탕 게임

# Function finding max_value
def find_max():
    global N, board

    # row 행
    max_value1 = 0 # 행행에서의 최댓값을 저장할 변수

    for i in range(N):
        c = "V" # 직전 문자 저장 변수. 그래서 board에는 없는 값으로 초기값을 설정
        cnt = 0
        for j in range(N):
            if board[i][j] == c: # 이전 문자와 같다면 원래 카운트에서 1증가
                cnt += 1
            else: # 이 문자가 직전에 없었으면 카운트는 1
                cnt = 1
                c = board[i][j] # 방금 나온 문자를 저장    
            
            max_value1 = max(max_value1, cnt)

    # column 열
    max_value2 = 0 # 열에서의 최댓값을 저장할 변수

    for i in range(N):
        c = "V" # 직전 문자 저장 변수. 그래서 board에는 없는 값으로 초기값을 설정
        cnt = 0
        for j in range(N):
            if board[j][i] == c:
                cnt += 1
            else:
                cnt = 1
                c = board[j][i] # 방금 나온 문자를 저장
            
            max_value2 = max(max_value2, cnt)
    
    return max(max_value1, max_value2)

# input
N = int(input())
board = [list(input()) for _ in range(N)]

# 방향벡터 동-서-남-북순
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_value = 0 # 최댓값을 넣어서 출력할 변수수

# 이중 반복문은 좌표를 하나씩 돌아가기 위해
for y in range(N):
    for x in range(N):
        
        for i in range(4): # 상하좌우 확인을 위해
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N: # 범위를 벗어나지 않는지 체크
                if board[y][x] != board[ny][nx]: # 옮길 값이라 바꿀 값이 다를때만 통과/ 같은 경우는 바꿀 필요가 없음
                    
                    # 먼저 두 값을 바꾼다 -> 행과 열을 확인해서 최댓값을 찾는다 -> 다시 자리를 원위치 시킨다
                    board[ny][nx], board[y][x] = board[y][x], board[ny][nx]
                    max_value = max(max_value, find_max())
                    board[ny][nx], board[y][x] = board[y][x], board[ny][nx]

print(max_value)