def solution(sizes):
    w = 0
    h = 0
    for i in range(len(sizes)):
        if max(sizes[i][0],h) * max(sizes[i][1],w) < max(sizes[i][0],w) * max(sizes[i][1],h):
            w = max(sizes[i][1],w)
            h = max(sizes[i][0],h)
        else:
            w = max(sizes[i][0],w)
            h = max(sizes[i][1],h)
    answer = w*h
    return answer
