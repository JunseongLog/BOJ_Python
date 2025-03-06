# 백준 12865번 평범한 배낭
# 이거 못 풀었음.

# 물건의 수N, 버틸수 있는 무게K
N, K = map(int, input().split())

# 정보를 입력 받을 리스트트
infos = [[0, 0]] # 맵핑을 위해 0, 0을 추가
for i in range(N):
    infos.append(list(map(int, input().split())))

# dp 리스트
dp = [[0]*(K+1) for _ in range(N+1)]

for k in range(1, N+1):
    for w in range(1, K+1):
        if w >= infos[k-1][0]:
            dp[k][w] = max(dp[k-1][w], infos[k-1][1] + dp[k-1][w-infos[k-1][0]])
        else:
            dp[k][w] = dp[k-1][w]

print(dp[N][K])