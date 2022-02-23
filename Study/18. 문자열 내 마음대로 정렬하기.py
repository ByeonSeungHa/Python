def solution(strings, n):
    strings.sort()
    answer = []
    list_1 = []
    for i in range(len(strings)):
        list_1.append(list(strings[i]))
    list_1.sort(key=lambda x: (x[n]))

    for i in range(len(list_1)):
        answer.append(''.join(list_1[i]))

    return answer