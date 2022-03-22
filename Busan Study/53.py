# 문제
#
# def solution(scores):
#     count = 0
#     for s in scores:
#         if 650 <= s or s < 800:
#             count += 1
#     return count
#
# #The following is code to output testcase. The code below is correct and you shall correct solution function.
# scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
# ret = solution(scores)
#
# #Press Run button to receive output.
# print("Solution: return value of the function is", ret, ".")

# 내 답

# def solution(scores):
#     count = 0
#     for s in scores:
#         if 650 <= s and s < 800:
#             count += 1
#     return count

# 풀이

def solution(scores):
    count = 0
    for i in range(len(scores)):
        if 650 <= scores[i] < 800:
            count += 1
    return count