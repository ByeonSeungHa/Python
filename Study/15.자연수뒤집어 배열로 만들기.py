def solution(n):

    n = int(n)
    n = list(str(n))
    b = list(reversed(n))
    c = list(map(int, b))
    answer = c

    return answer