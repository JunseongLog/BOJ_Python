# 백준 1912번 연속합

N = int(input())
arr = [0] + list(map(int, input().split()))

# dp[n]: n까지의 연속된 값의 합의 최댓값
dp = [0 for _ in range(N+1)]

#kadane' algorithm 연속 부분 수열의 최대합 알고리즘
for i in range(1, N+1):
    dp[i] = max(dp[i-1], 0) + arr[i]

# 슬라이싱을 하는 이유는 dp[0]이 쓰는 값이 아니여서서
print(max(dp[1:]))