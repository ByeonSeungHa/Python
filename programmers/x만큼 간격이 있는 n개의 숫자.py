def solution(x, n):
    answer = []
    if x == 0:
        return [0 for i in range(n)]
    for i in range(x, x * (n + 1), +x):
        answer.append(i)
    return answer
solution

