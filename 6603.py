# 백준 6603번 로또 (집합 유형문제)

def combination(index, level):
    global choose, k, lst

    if level == 6:
        print(" ".join(map(str, choose)))
        return
    
    for i in range(index, k):
        choose.append(lst[i]) # 현재 인덱스 자리 값을 배열에 추가
        combination(i+1, level+1) # 위에서 배열에 값을 넣었고, if 문으로 걸러지기면서 6 조합을 계속 만든다  
        choose.pop() # 넣었던 값을 빼준다


while True:

    value = list(map(int, input().split())) # 입력 받기

    # 값의 갯수 k, 값의 원소 배열 lst
    k = value[0]
    lst = value[1:]

    # k == 0이면 종료
    if k == 0:
        break
    
    # 배열 choose선언 = global을 써야함함
    choose = []
    combination(0, 0) # index, level
    print() # 공백
