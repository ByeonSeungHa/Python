def solution(participant, completion):
    answer = ''
    dic1 = {}
    dic2 = {}
    for i in range(len(participant)):

        if participant[i] not in dic1:
            dic1[participant[i]] = 0
        elif participant[i] in dic1:
            dic1[participant[i]] += 1
    for j in range(len(completion)):
        if completion[j] not in dic2:
            dic2[completion[j]] = 0
        elif completion[j] in dic2:
            dic2[completion[j]] += 1
    for t in dic1:
        if t not in dic2:
            return t
        if dic1.get(t) != dic2.get(t):
            return t
    return t