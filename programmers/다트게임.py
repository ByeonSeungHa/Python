def solution(dartResult):
    answer = []
    sutza = ['0','1','2','3','4','5','6','7','8','9','10']
    for i in range(len(dartResult)-1):
        if dartResult[i] == 'S' and dartResult[i+1] != '*' and dartResult[i+1] != '#':
            point *= 1
            answer.append(point)
        elif dartResult[i] == 'S' and dartResult[i + 1] == '#':
            point = point ** 1
        elif dartResult[i] == 'S' and dartResult[i + 1] == '*':
            point = point ** 1
        elif dartResult[i] == 'D' and dartResult[i+1] != '*' and dartResult[i+1] != '#':
            point = point ** 2
            answer.append(point)
        elif dartResult[i] == 'D' and dartResult[i + 1] == '#':
            point = point ** 2
        elif dartResult[i] == 'D' and dartResult[i+1] == '*':
            point = point ** 2
        elif dartResult[i] == 'T' and dartResult[i+1] != '*' and dartResult[i+1] != '#':
            point = point ** 3
            answer.append(point)
        elif dartResult[i] == 'T' and dartResult[i + 1] == '#':
            point = point ** 3
        elif dartResult[i] == 'T' and dartResult[i + 1] == '*':
            point = point ** 3
        elif dartResult[i] == '*':
            if len(answer)==0:
                answer.append(point * 2)
            else :
                answer[-1] = answer[-1] * 2
                answer.append(point*2)
        elif dartResult[i] == '#':
            point = -point
            answer.append(point)
        elif dartResult[i] == '1' and dartResult[i+1] == '0':
            point = 10
        elif dartResult[i] == '0' and dartResult[i-1] == '1':
            continue
        elif dartResult[i] in sutza:
            point = sutza.index(dartResult[i])
    if dartResult[-1] == 'T':
        answer.append(point**3)
    elif dartResult[-1] == 'S':
        answer.append(point**1)
    elif dartResult[-1] == 'D':
        answer.append(point**2)
    elif dartResult[-1] == '*':
        answer[-1] = answer[-1] * 2
        answer.append(point*2)
    elif dartResult[-1] == '#':
        answer.append(-point)

    return sum(answer)



dartResult ='1T2D3D#'
solution(dartResult)
