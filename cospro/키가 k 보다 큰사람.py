# 틀린부분을 고쳐라
# 전
def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h >= k:
            answer += 1
    return answer
# 후
def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h > k:
            answer += 1
    return answer