# 하샤드 수 란? 각 자릿수를 더해서 원래의 수를 나눴을 때 나누어지는 수를 하샤드 수라고 한다.
def solution(x):
    answer = True
    x = str(x)
    sum = 0
    y = 0
    for i in range(len(x)):
        sum += int(x[i])
        if int(x)%sum == 0:
            answer = True
        else :
            answer = False
    return answer


# 간단한 수식
# y = sum(map(int,(list(str(x)))))
# if int(x)%y == 0:
#     return True
# else :
#     return False
