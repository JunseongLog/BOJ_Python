# 조합 5C3 구하기
# 재귀함수 사용

lst = [1, 2, 3, 4, 5] # 원소
choose = [] # 뽑아서 여기에 넣어준다

def combination(index, level):
    if level == 3:
        print(choose)
        return
    
    for i in range(index, 5): # 원소의 마지막 인덱스 값이 4니까
        choose.append(lst[i])
        combination(index + 1, level + 1)
        choose.pop()

combination(0, 0)



"""
# 반복문 사용

N = 5 #원소의 총 개수

lst = [1, 2, 3, 4, 5]
choose = []

for i in range(0, N):
    choose.append(lst[i])
    for j in range(i+1, N):
        choose.append(lst[j])
        for k in range(j+1, N):
            choose.append(lst[k])
            print(choose)
            choose.pop()
        choose.pop()
    choose.pop()
"""
