# 백준 1149번 RGB거리

N = int(input())

# dp역할을 하는 min_cost리스트

cost = [[0, 0, 0]] # 인덱스 맵핑을 위해서 0번 인덱스 추가
for _ in range(N):
    cost.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(N+1)]

# dp 1번인덱스 초기화
dp[1][0] = cost[1][0]
dp[1][1] = cost[1][1]
dp[1][2] = cost[1][2]

# 각 인덱스별 최소 비용 구하기
# 모든 경우를 모두 구해줄거다. 3가지 중에 어디로 갈지를 모르니 모두 구하고 결과값만 비교할 거임임
for i in range(2, N+1):
    # dp[i][0], dp[i-1][0] 같은 자리 이전 제외외
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]

    # dp[i][1]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]

    # dp[i][2]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N]))