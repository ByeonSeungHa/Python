def solution(strings, n):
    strings.sort()
    answer = []
    temp = []
    for i in range(len(strings)):
        print(strings[i])
        temp.append(list(strings[i]))
    temp.sort(key=lambda x : (x[n]))
    for j in range(len(temp)):
        answer.append( ''.join(temp[j]))
    print(answer)
    return answer