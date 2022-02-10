def solution(id_list, report, k):
    report2 = list(set(report)) # 중첩 없애주기
    singoza = {}
    gahaeza = {}
    list_2 = []
    answer = []
    for i in range(len(id_list)):
        singoza[id_list[i]] = 0
        gahaeza[id_list[i]] = 0
    for i in range(len(report2)):
        q = report2[i].split(" ")
        gahaeza[q[1]] += 1
    for i in gahaeza:
        if gahaeza.get(i) >= k:
            list_2.append(i)
    for i in range(len(report2)):
        q = report2[i].split(" ")
        if q[1] in list_2:
            singoza[q[0]] += 1

    for i in singoza:
        answer.append(singoza.get(i))

    return answer