def solution(lottos, win_nums):
    answer = []
    manhi = 0
    juckgae = 0
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == 0:
                manhi += 1
                break
            else:
                if lottos[i] == win_nums[j]:
                    manhi += 1
                    juckgae += 1
    if manhi == 6:
        answer.append(1)
    elif manhi == 5:
        answer.append(2)
    elif manhi == 4:
        answer.append(3)
    elif manhi == 3:
        answer.append(4)
    elif manhi == 2:
        answer.append(5)
    else:
        answer.append(6)

    if juckgae == 6:
        answer.append(1)
    elif juckgae == 5:
        answer.append(2)
    elif juckgae == 4:
        answer.append(3)
    elif juckgae == 3:
        answer.append(4)
    elif juckgae == 2:
        answer.append(5)
    else:
        answer.append(6)
    print(manhi, juckgae)

    return answer