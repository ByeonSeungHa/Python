def solution(s):
    if len(s) %2 ==1:
        answer = s[len(s)//2]
    else:
        answer = s[(len(s)//2)-1] + s[(len(s)//2)]
    return answer
# def solution(s):
#     n = s[len(s)//2]
#     if len(s) %2 ==1:
#         answer = n
#     else:
#         answer = s[(len(s)//2)-1] + n
#     return answer