# a: 합을 구해야 하는 정수 n개가 저장 되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함 되어 있는 정수 n개의 합 (정수)
def solve(a): # sum을 이용한 간단한 식
     return sum(a)

def solve(a): # for 문을 돌려 더한 식
    plus = 0
    for i in a:
        plus += i
    return plus
