# BOJ 1620번 나는야 포켓몬 마스터 이다솜

poketmon = []
poketmon_name = {}

n, m = map(int, input().split())

for i in range(n):
    name = input()
    poketmon_name[name] = i + 1 # key값과 맵핑을 위해
    poketmon.append(name)

for i in range(m):
    value = input()
    # 들어온 값이 알파벳일때
    if value.isalpha():
        print(poketmon_name[value])
    # 들어온 값이 숫자일때
    else:
        print(poketmon[int(value)-1])
