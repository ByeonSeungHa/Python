S = input()
alphabet = list(range(97,123))
# 아스키 코드를 사용한다.
# 97~122까지가 a~z이다.
# 65~90까지가 A~Z이다.
for i in alphabet:
    print(S.find(chr(i)))

# 아스키코드를 숫자 -> 문자는 chr()함수이고
# 아스키코드를 문자 -> 숫자는 ord()함수이다.