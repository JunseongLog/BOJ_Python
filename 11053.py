# 백준 11053번 가장 긴 증가하는 부분 수열

N = int(input())
arr = list(map(int, input().split()))

#dp리스트 초기값은 모두 1이다. 어떤 값에서 시작하든 일단 자신을 포함해서 1이기 때문에
dp = [1] * N

for i in range(1,N): # 1부터 시작하는 이유: 0부터 시작하면 안에 있는 반복문이 어차피 안돌아감
    for j in range(i): # i를 끝값으로 줘서 i전에 있는 값만 탐색한다
        
        if arr[i] > arr[j]: # i번째보다 그전 값이 작을때마다
            dp[i] = max(dp[i], dp[j]+1) # 이어져온 부분집합에 1을 더한게 현재dp값이니까 두개를 비교 해서 대입입

print(max(dp))