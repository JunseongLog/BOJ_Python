# 백준 1018번 체스판 다시 칠하기

# 체스판 두개를 비교해서 더 작은 값을 반환하는 함수
def get_min(y, x):
    cnt1 = 0 # 체스판1을 비교해서 다른 값을 카운트
    cnt2 = 0 # 체스판2를 비교해서 다른 값을 카운트

    for i in range(8):
        for j in range(8):
            if chess1[i][j] != board[y+i][x+j]:
                cnt1 += 1
            if chess2[i][j] != board[y+i][x+j]:
                cnt2 += 1

    return min(cnt1, cnt2)


# 체스판 크기 세로N, 가로로M
N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 시작이 W인 체스판/ B인 체스판 두개가 있으니까 두개를 만든다
chess1 = [["" for _ in range(8)] for _ in range(8)]
chess2 = [["" for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        chess1[i][j] = "W" if (i+j)%2 == 0 else "B"
        chess2[i][j] = "B" if (i+j)%2 == 0 else "W"

# 8*8로 자르는 경우의 수
min_count = int(1e9) 
# DFS처럼 조건에 맞으면 좌표값을 사용자정의 함수에 넣어서 함수 호출
# 체스판을 두개를 비교해서 둘중에 더 작은 것이 반환되도록 한다
# N-7, M-7을 해주면 조건문없이/ 인덱스 에러 없이 자를 수 있는 경우만 통과하기 때문문
for i in range(N - 7):
    for j in range(M - 7):
        min_count = min(min_count, get_min(i, j))

print(min_count)