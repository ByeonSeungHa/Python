def solution(n, m):
    answer = []
    yarksoo1 = 0
    dict1 = {}
    baesoo1 = 1
    list_1 = yarksoo(n)
    list_2 = yarksoo(m)
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                yarksoo1=max(yarksoo1, list_1[i])
    list_3 = baesoo(n)
    list_4 = baesoo(m)
    for i in range(len(list_3)):
        if list_3[i] not in dict1:
            dict1[list_3[i]] = list_3.count(list_3[i])
    for i in range(len(list_4)):
        if list_4[i] not in dict1:
            dict1[list_4[i]] = list_4.count(list_4[i])
        else :
            if dict1.get(list_4[i]) < list_4.count(list_4[i]):
                dict1[list_4[i]] = list_4.count(list_4[i])
    for i in dict1:
        baesoo1 = baesoo1 * i ** dict1.get(i)
    answer.append(yarksoo1)
    answer.append(baesoo1)

    return answer
def yarksoo(n): # 0으로 나누면 무한대가 된다.
    yarksoo_list = []
    for i in range(1, n+1) :
        if n % i == 0:
            yarksoo_list.append(i)
    return yarksoo_list
def baesoo(m) :
    baesoo_list = []
    while m != 1:
        for i in range(2,m+1):
            if m % i == 0:
                m = m//i
                baesoo_list.append(i)
                break
    return baesoo_list
