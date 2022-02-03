def solution(s):
    answer = ''
    s2 = s.split(" ")
    a = []
    for i in range(len(s2)):
        temp = ""
        for j in range(len(s2[i])):

            if j % 2 == 0:
                temp += s2[i][j].upper()
            else:
                temp += s2[i][j].lower()
        a.append(temp)
    answer = ' '.join(a)
    print(answer)
    return answer