# 순열 로직

# 인덱스를 따로 인자로 받을 필요가 없음. 
# check배열로 현재 몇번째 값이 사용중인지 알 수 있기 때문
def permutation(level):
    global R
    if level == R:
        print(choose)
        return
    
    # 조합엔 인자로 (index, N)이지만, 순열은 0부터여서 N값만 넣는다
    for i in range(N):

        choose.append(lst[i])
        check[i] = True 

        permutation(level+1)

        check[i] = False
        choose.pop()

# 순열: N"P"R 에서의 각 값들
N = 10
R = 3
# lst에 들어있는 원소들
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
choose = [] # 여기로 원소를 뽑아서 넣어준다다
check = [False] * N # 선택된 값을 표시하기 위한 배열

permutation(0) # level
