# 에라토스테네스의 체(파이썬)

def solution(n):
    a = [True] * (n + 1) # [ True, True ....]
    m = int(n**0.5)  # 소수 판별 범위.
    for i in range(2, m + 1):
        if a[i] == True: # a[i]가 True일때
            for j in range(i + i, n + 1, i): # 출발 지점, 도착지점, i만큼 증가
                a[j] = False # 소수가 아니면 False
    answer =(len([i for i in range(2, n + 1) if a[i] == True])) # 2부터 n+1까지로 범위 조정 0과1은 소수가 아니다.
    return answer




# 다른 방법

# def solution(n):
#     count = 0
#     answer = 0
#     for i in range(2,n+1):
#         for j in range(2,i+1):
#             if i%j == 0:
#                 count += 1
#         if count == 1:
#             answer += 1
#         count = 0
#    return answer