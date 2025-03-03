# 백준 11048번 이동하기

# 0. 입력받기기
N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

# 1. dp리스트 만들기기
dp = [[0] * M for _ in range(N)]

# 2. dp의 1행과 1열에 값을 넣는다다
dp[0][0] = matrix[0][0] # 첫dp값은 입력된 첫값과 같음

for i in range(1, M): # 1행 값넣기 
    dp[0][i] = dp[0][i-1] + matrix[0][i]

for j in range(1, N): # 1열 값넣기기
    dp[j][0] = dp[j-1][0] + matrix[j][0]

# 3. 나머지 값 구해서 dp에 채워넣기기
# 1행/1열을 제외한 나머지 값 넣기
# 한점으로 갈 수 있는 경우가 세개, 그중에 가장 큰 값을 dp리스트에 해당 좌표에 넣는다

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]

print(dp[N-1][M-1])