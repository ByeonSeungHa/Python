# 틀린부분을 고쳐라
# 전
def solution(s):
    s_lst = list(s)
    n = len(s)
    for i in range(n):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        if s_lst[i] == 'z':
            s_lst[i] =  'a'
    return "".join(s_lst)
후
def solution(s):
    s_lst = list(s)
    n = len(s)
    for i in range(n):
        if s_lst[i] == 'a':
            s_lst[i] = 'z'
        elif s_lst[i] == 'z':
            s_lst[i] =  'a'
    return "".join(s_lst)