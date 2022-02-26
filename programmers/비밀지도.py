def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        a  = str(bin(arr1[i])[2:])
        while  len(a) != n:
            a = '0' + a
        b = str(bin(arr2[i])[2:])
        while len(b) != n:
            b = '0' + b
        list_a = list(map(int,list(a)))
        list_b = list(map(int,list(b)))
        list_c = []
        for i in range(len(list_a)):
            if list_a[i]+list_b[i] == 0:
                list_c.append(' ')
            else :
                list_c.append('#')
        answer.append(''.join(list_c))


    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n,arr1,arr2)
# print(bin(11)) = 0b 1011 2법으로 변환이다(0b)