# BOJ 4659번 비밀번호 발음하기

lst = ["a", "e", "i", "o", "u"]

while True:

    password = input()

    if (password == "end"):
        break
    
    # 모음 하나 포함하는지 확인
    count = 0
    for i in password:
        if i in lst:
            count += 1
    
    if count < 1:
        print(f"<{password}> is not acceptable.")
        continue

    # 모음이 3개 혹은 자음이 3개 연속인지 확인
    count2 = 0
    for i in range(len(password)-2):
        if (password[i] in lst and password[i+1] in lst and password[i+2] in lst):
            count2 = 1
        elif not(password[i] in lst) and not(password[i+1] in lst) and not(password[i+2] in lst):
            count2 = 1
    
    if count2 == 1:
        print(f"<{password}> is not acceptable.")
        continue

    # 같은 글자가 연속적으로 두번 오는지 확인
    count3 = 0
    for i in range(len(password)-1):
        if (password[i] == password[i+1]):
            if password[i] == "e" or password[i] == "o":
                continue
            else:
                count3 = 1
    
    if count3 == 1:
        print(f"<{password}> is not acceptable.")
        continue

    print(f"<{password}> is acceptable.")





