# 백준 1759번 암호 만들기

vowel_lst = ['a', 'e', 'i', 'o' ,'u']

def is_possible():
    global need_value_num, choose

    vowel = 0
    
    for c in choose: # choose에서 문자 하나씩 빼면서
        if (c in vowel_lst):
            vowel += 1
    consonant = need_value_num - vowel

    return (consonant >= 2 and vowel >= 1)


def combination(index, level):
    global lst, need_value_num, total_value_num
    if level == need_value_num:
        if is_possible(): # 모음 1개 이상, 자음 두개 이상인지 확인하는 함수
            print("".join(choose))
        return
    
    for i in range(index, total_value_num):
        choose.append(lst[i])
        combination(i+1, level+1)
        choose.pop()


# 순서대로 조합에 필요한 수, 원소의 총 개수
need_value_num, total_value_num = map(int, input().split())
lst = list(input().split())

if need_value_num == 0 or total_value_num == 0:
    exit()

# 리스트로 받은 것을 사전순으로 정렬해야 한다. 신기하게 문자열도 sort()함수가 가능
lst.sort()

choose = []
combination(0, 0) # index, level