def solution(arr, k):
    answer = 0
    s = []
    for i in arr:
        for j in i:
            s.append(j)
    answer = sorted(s)
    answer = answer[k-1]
    return answer