# 백준 5585번 거스름돈

change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

count = 0

for coin in coins:
    count += change // coin # count에 몫
    change = change % coin # change는 코인으로 나눈 나머지

print(count)