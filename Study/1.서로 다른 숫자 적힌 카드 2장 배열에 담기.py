# 2. 자연수가 적힌 2 X N장의 카드묶음. 같은 숫자가 적힌 카드 2장씩 포함
# 서로 다른 숫자가 적힌
# 잃어버린 서로 다른 숫자 적힌 카드 2장 배열에 담기
# [1, 3, 2, 5, 3, 1] -> [2, 5]
# [1, 2, 3, 4, 4, 3, 2, 5] -> [1, 5]
def solution(N):
    dic = {}
    answer = []
    for i in range(len(N)):
        dic[N[i]] = N.count(N[i])
    print(dic)
    for j in dic:
        if dic.get(j) == 1: # set 기능이 들어가있다.
            answer.append(j)
    print(answer)
    return answer


N = [1, 3, 2, 5, 3, 1]
solution(N)
