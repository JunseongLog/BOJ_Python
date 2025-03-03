# 백준 1461번 도서관

# 책의 개수N, 한번에 들 수 있는 책의 개수M
N, M = map(int, input().split())
arr = map(int, input().split())

# 양수/음수를 각각 넣어줄 배열
positive = []
negative = []

for value in arr:
    if value > 0: # 양수면 positive
        positive.append(value)
    else: # 음수면 negative
        negative.append(-value) # 값을 양수로 전환해서 넣어준다

# 내림차순으로 정렬
positive = sorted(positive, reverse=True)
negative = sorted(negative, reverse=True)

distance = []

# 처음부터 끝까지 M을 스텝으로 꺼낸다
for step in positive[::M]: # 양수 값 처리
    distance.append(step)

for step in negative[::M]: # 음수 값 처리(이전에 부호 바꿔서 양수이긴 하다)
    distance.append(step)

total_sum = 0
# 마지막 값을 가면 돌아올 필요가 없다. 어쨋든 최단거리면 가장큰 값을 마지막에 간다고 생각하고 제외해야 하는듯
total_sum = 2 * sum(distance) - max(distance)

print(total_sum)