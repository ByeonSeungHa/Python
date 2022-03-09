def solution(price, money):
    answer = 0
    s = 0
    for i in price:
        s = s+i
        if s>money:
            return -1
        else :
            answer = money - s
    return answer