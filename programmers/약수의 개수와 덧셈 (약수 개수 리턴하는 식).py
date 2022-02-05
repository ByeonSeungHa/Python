def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if count(i)%2 == 0 :
            answer += i
        elif count(i)%2 == 1:
            answer -= i
    return answer

# 약수 갯수 확인하는 식
def count(n):
    count = []
    answer = 0
    for i in range(1,n+1):
        if n % i == 0: # 약수인지 확인하는 식
            count.append(i)
    return len(count) # 약수의 갯수 리턴