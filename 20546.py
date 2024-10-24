#BOJ 문제 20546번 기적의 매매법

# 준현이의 주식 매도 매수
def bnp(stock_price, cash):
    having_stock = 0
    left_cash = cash
    for price in stock_price:
        # 보유 현금으로 주식을 살 수 있다면
        if left_cash // price > 0:
            # 보유 주식은 몫을 담고
            having_stock += left_cash // price
            # 현금에는 나머지를 담는다
            left_cash %= price
    
    return having_stock * stock_price[-1] + left_cash

# 성민이의 주식 매도 매수
def timing(stock_price, cash):
    having_stock = 0
    left_cash = cash

    for i in range(3, len(stock_price)):

        action = what_to_do(stock_price, i)

        if action == "buy":
            if left_cash >= stock_price[i]:
                having_stock += left_cash // stock_price[i]
                left_cash %= stock_price[i]
        if action == "sell":
            if having_stock > 0:
                left_cash += having_stock * stock_price[i]
                having_stock = 0
    
    return having_stock * stock_price[-1] + left_cash

# timing함수에서 사용되는 의사를 결정하는 함수
def what_to_do(stock_price, i):
    
    if (stock_price[i-1] > stock_price[i-2] and stock_price[i-2] > stock_price[i-3]):
        return "sell"
    elif (stock_price[i-1] < stock_price[i-2] and stock_price[i-2] < stock_price[i-3]):
        return "buy"
    return "hold"




cash = int(input())
stock_price = list(map(int, input().split()))

if (bnp(stock_price, cash) > timing(stock_price, cash)):
    print("BNP")
elif (bnp(stock_price, cash) < timing(stock_price, cash)):
    print("TIMING")
elif (bnp(stock_price, cash) == timing(stock_price, cash)):
    print("SAMESAME")