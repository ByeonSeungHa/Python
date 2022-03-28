def solution(participant, completion):
    answer = ''
    dic1 = {}
    dic2 = {}
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if participant[i] not in dic1:
            dic1[participant[i]] = 1
        else:
            dic1[participant[i]] += 1
    for i in range(len(completion)):
        if completion[i] not in dic2:
            dic2[completion[i]] = 1
        else:
            dic2[completion[i]] += 1

    for i in dic1:
        if dic1.get(i) != dic2.get(i):
            return i