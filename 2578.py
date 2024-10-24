#BOJ 문제 2578

def bingo(arr):

    bingo_number = 0

    # 가로가 빙고일 때
    for i in arr:
        if i.count(0) == 5:
            bingo_number += 1

    # 세로 빙고 컨프리헨션
    
    for i in range(5):
        if all(arr[j][i] == 0 for j in range(5)):
            bingo_number += 1
    
    
    # 대각선 컨프리헨션
    if all(arr[i][i] == 0 for i in range(5)):
        bingo_number += 1

    
    # 대각선 2 컨프리헨션
    if all(arr[i][4-i] == 0 for i in range(5)):
        bingo_number += 1

    return bingo_number 


# 빙고판 입력 받기
game_map = []
for i in range(5):
    game_map.append(list(map(int, input().split())))

called_numbers = []
for _ in range(5):
    called_numbers.extend(map(int, input().split()))

# 3줄 빙고가 되려면 최소 12개는 되어야 함. 그걸 카운트하기 위한 변수
# 그리고 이 변수를 통해 몇번째 호출에서 빙고가 되었는지도 알 수 있음
count = 0

for value in called_numbers:
    for i in range(5):
        for j in range(5):
            if game_map[i][j] == value:
                game_map[i][j] = 0
                # 값이 일치할때마다 값을 0으로 바꾸고 카운트
                count += 1
    
    # 세 줄 빙고의 최솟값인 12개 이상부터는 bingo함수를 통해 빙고인지 확인함
    if count >= 12:
        if bingo(game_map) >= 3:
            print(count)
            break
        