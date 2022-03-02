def solution(dartResult):
    answer = 0
    bunsu = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    dart = []
    for i in range(len(dartResult)):
        if dartResult[i] in bunsu:
            value = bunsu.index(dartResult[i])

            if dartResult[i] == '1' and dartResult[i + 1] == '0':
                dart.append(10)
                continue
            if dartResult[i] == '0' and dartResult[i - 1] == '1':
                continue
            dart.append(value)
        if dartResult[i] == 'S':
            dart[-1] = dart[-1] ** 1

        elif dartResult[i] == 'D':
            dart[-1] = dart[-1] ** 2

        elif dartResult[i] == 'T':
            dart[-1] = dart[-1] ** 3

        if dartResult[i] == '*':
            if len(dart) == 1:
                dart[0] = dart[0] * 2
            else:
                dart[-1] = dart[-1] * 2
                dart[-2] = dart[-2] * 2
        if dartResult[i] == '#':
            dart[-1] = dart[-1] * -1

    print(dart)

    return sum(dart)