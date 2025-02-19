# 백준 10974번 모든 순열

def permutation(level):
    global N, array, choose

    if level == N:
        print(" ".join(map(str, choose)))
        return

    for i in range(N):

        # 인덱스 i인 원소가 이미 사용중이라면 continue
        if check[i] == True: 
            continue
        
        choose.append(array[i]) # 인덱스 i인 원소를 추가
        check[i] = True # 인덱스 i의 원소가 사용중이므로 True로 초기화

        permutation(level+1) # 재호출을 하면서 다음 자리의 숫자를 선택한다.

        check[i] = False # 인덱스 i인 원소의 사용이 끝났으므로 False로 초기화
        choose.pop() # 인덱스 i인 원소를 배열에서 제거


N = int(input())

check = [False] * N
array = [] # 원소를 넣어줄 리스트
choose = [] 
for i in range(N):
    array.append(i+1)

permutation(0)