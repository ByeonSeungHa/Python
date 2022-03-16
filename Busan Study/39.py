# 문제

# def solution(number):
#     count = 0
#     while number >= 0:
#         n = number % 10
#         if n == 2 or n == 3 or n == 5 or n == 7:
#             count += 1
#         number //= 10
#     return count

# 답

def solution(number):
    count = 0
    while number:
        n = number % 10
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        number //= 10
    return count