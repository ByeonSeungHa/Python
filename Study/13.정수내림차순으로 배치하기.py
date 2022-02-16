def solution(n):
    n = int(n)
    a = list(str(n))
    a.sort(reverse = True)
    answer = "".join(a)
    return int(answer)