# 문제
#
# def solution(data):
#     total = sum(data)
#     average = len(data) / total
#     cnt = 0
#     for d in data:
#         if d <= average:
#             cnt += 1
#     return cnt

# 답

def solution(data):
    total = sum(data)
    average = total / len(data)
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt

