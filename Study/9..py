import operator
def solution(N, stages): # 효율성에 자주 사용하는 식
    dic = {}
    dic2 = {}
    boonmo = 0
    answer = []
    for i in range(len(stages)):
        if stages[i] not in dic:
            dic[stages[i]] = 1
        else :
            dic[stages[i]] += 1
    for j in dic:
        for j2 in dic:
            if j2 >= j and N <= j:
                boonmo += dic.get(j2)
            elif j2 >= N > j:
                if boonmo != 0:
                    dic2[j] = 0 / boonmo

        print(boonmo)
        if boonmo != 0:
            dic2[j] = dic.get(j)/boonmo

        boomo = 0
    sdic = sorted(dic2.items(), key=operator.itemgetter(0))
    sdic = list(map(list, sdic))
    sdic.sort(key=lambda x : (-x[1], x[0]))
    print(sdic, "asdfasf")

    for i in range(1, N+1):
        if i in dic2:
            answer.append(dic2.get(i))
        else:
            answer.append(0)
    print(answer)

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)