# 백준 23246 Sport Climbing Combined

def comp(x):
    return (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0])

# 선수 인원수
N = int(input())
# b번호 p, q, r 각종목
info = [list(map(int, input().split())) for _ in range(N)]

# key에 들어가는 함수에서 순서대로 우선순위로 정렬한다.
# comp를 만들어서 쓰는 대신 lambda를 바로 써도 된다.
info = sorted(info, key=comp)

# 3등까지만 출력하면 된다다
for b, p, q, r in info[:3]:
    print(b, end=" ")