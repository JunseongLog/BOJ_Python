# BOJ 2979번 트럭 주차

# 각 시간마다 트럭이 몇대 있는지 구분할 리스트
time_list = [0] * 101

# 트럭 개수마다 요금
a, b, c = map(int, input().split())

for i in range(3):
    start, end = map(int, input().split())
    # end + 1이 아닌 이유는 end는 떠난 시간이기에 카운트 x
    for j in range(start, end):
        time_list[j] += 1

sum = 0

for i in range(1, 101):
    if time_list[i] == 1:
        sum += a
    elif time_list[i] == 2:
        sum += (b * 2)
    elif time_list[i] == 3:
        sum += (c * 3)
    else:
        continue

print(sum)