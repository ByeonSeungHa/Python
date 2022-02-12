def solution(s):
    answer = ''
    s2 = s.split(" ")
    a = []
    for i in range(len(s2)):
        temp = ""
        for j in range(len(s2[i])):
            if j%2 == 0:
                temp += s2[i][j].upper()
            elif j%2 == 1:
                temp += s2[i][j].lower()
        a2 = ''.join(temp)
        a.append(a2)
    answer = ' '.join(a)
    print(a)

    return answer