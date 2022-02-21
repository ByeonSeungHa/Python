# n진수를 10진법으로 변환하는 방법이다.
#
# int(string, base)
#
# 위와 같은 형식으로 사용. base에는 진법을 넣으면 된다.
# print(int('101',2))
# print(int('202',3))
# print(int('303',4))
# print(int('404',5))
# print(int('505',6))
# print(int('ACF',16))

# n진수를 2,8,16진법으로 변환하는 방법이다.
# print(bin(11)) = 0b 1011 2법으로 변환이다(0b)
# print(oct(11)) = 0o13 8진법으로 변환이다.(0o)
# print(hex(11)) = 0xb 16진법으로 변환이다.(0x)

# 진법표시를 없애려면 [2:]를 붙이면 된다.

# print(bin(11)[2:]) = 1011
# print(oct(11)[2:]) = 13
# print(hex(11)[2:]) = b

# n진수를 다른 n진수로 바꾸는 방법은 우선 n진수를 10진수로 바꾸고 다시 n진수로 바꾸면 된다.

# print(solution(int('c',16),4))  16진수인 C를 4진수로 바꾸는것
# print(solution(int('4',6),3))   6진수인 4를 3진수로 바꾸는것
# print(solution(int('21',3),7))  3진수인 21을 7진수로 바꾸는것
# print(solution(int('15',9),5))  9진수인 15를 5진수로 바꾸는것