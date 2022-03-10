# 거스름돈

def solution(price, money):
    answer = 0
    s = 0
    for i in price:
        s += i
        if i > money:
            return -1
        else :
            answer = money - s
    return answer

price =[2100, 3200, 2100, 800]
money = 10000
solution(price, money)