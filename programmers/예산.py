def solution(d, budget):

    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:

            return i

    return i+1



d = [2,2,3,3]
budget = 10
solution(d, budget)