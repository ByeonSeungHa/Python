# 변수명 = 수식 또는 값 -> 변수
# 대소문자에 따라 달라진다.
# 언더바(_)입력 가능
# 예약어는 변수명으로 사용 불가능하다.
# 카멜 표기법 : 대문자 소문자로 단어 분리
# 스네이크 기법 : _,-단어 연결


# 변수 할당 방법
# 변수 = 수식 또는 값
x = 100
y = 500
print('x=', x)
print('y=', y)

y = 'HelloWorld'
print('y=',y)

# 쉼표(,)를 이용한 변수 할당
# 변수1, 변수2 = 값1, 값2
# 서로 다른 변수에 동일한 값 할당
userName, userAge = '홍길동', 33
print(userName, userAge)


# 예약어라서 변수 설정 불가능
# True = '참'

# 파이썬의 예약어 출력하기
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
# 변수 < 집합형 < 클래스 < 라이브러리 < 패키지

# 클래스명은 첫글자를 대문자로 표시
# 함수명은 소문자로 표시
# 변수명도 소문자로 시작

# 퀴즈 : user1, user2의 변수값을 서로 변경하여라
user1 = "영희"
user2 = "철수"
print('='*50)


# 중간변수 설정
temp = user1
user1 = user2
user2 = temp
print('user1=',user1)
print('user2=',user2)

print('='*50)


# 쉼표를 이용한 변수 교체
user1, user2 = user2, user1
print('user1=',user1)
print('user2=',user2)
print('='*50)




# 데이터형 확인하기
# type(변수/값) => 자료형이 정수인지 문자인지 리스트인지 말그대로 type을 알려준다.

# 자료형의 종류
# 기본자료형
# : 숫자형(정수, 실수)
# : 문자열형
# : 논리형 Boolean - True / False
# 집합자료형
# : 리스트, 튜플, 딕셔너리, 클래스, 집합

x=100
y=3.14
z=True
myString = 'abcd'
print('x=', x, type(x)) # 정수
print('y=', y, type(y)) # 실수
print('z=', z, type(z)) # 참 or 거짓
print('myString=', myString, type(myString))

print('='*50)

# 산술 연산자
# +, - , *, /, //(정수형 몫), %(나머지), **(제곱)

n1 = 33
n2 = 5
print(n1,'+', n2, '=', n1+n2)
print(n1,'-', n2, '=', n1-n2)
print(n1,'*', n2, '=', n1*n2)
print(n1,'/', n2, '=', n1/n2)
print(n1,'//', n2, '=', n1//n2)
print(n1,'%', n2, '=', n1%n2)
print(n1,'**2=', n1**2)

print('='*50)

# 대입 연산자
# 변수명 += , -= , *= , /=

a = 1

# a+=1
# -> a = a+1 # 2
# a-=1
# -> a= a-1 # 0
# a*=1
# -> a= a*1 # 1
# /=1
# -> a= a/1 # 1
# a//=1
# -> a= a//1 # 1
# a%=1
# -> a=a%1 # 1
# a**=1
# -> a= a**1 # 1

# 관계 연산자
# 결과값이 True / False
# ==, !=, >, <, >=, <=

x= 100
y= 10
z= 45

print(x==y,x !=y) # False True
print(x>=y,x <z) # True False

print('='*50)



# 논리 연산자
# and 는 둘다 True여야 True
# or 은 둘중 하나만 True여도 True
# not 은 True면 False, False면 True가 된다.
# 결과값이 True / False
# and, or, not
# 관계연산자를이용한수식1 논리 연산자 관계연산자를이용한수식2
# not(관계연산자를이용한수식)
x= 100
y= 10
z= 45

print((x>y) and (x>z)) # True
print((x<y) and (x<z)) # False
print((x<y) or (x>z)) # True
print((x<y) or (y>z)) # False
print(x==100, not(x==100)) # True False


print('='*50)

# 입력문
# 변수명 = input(메세지)
# 입력받은 변수는 데이터형이 문자열이다.

# userName = input('이름을 입력하여 주세요...')
# print(userName, '님 오늘도 좋은하루!!!!')

# 자료형 변환 = Casting
# int(값/수식/변수) : 정수형 데이터형으로 변환
# float(값/수식/변수) : 실수형 데이터형으로 변환
# str(값/수식/변수) : 문자열 데이터형으로 변환
# bool(값/수식/변수) : 논리형 데이터형으로 변환


# 나이를 입력받아서 출생년도를 출력하여라
# 나이(문자열) =>나이(정수형)
# 0은 False
# userAge = int(input('나이를 입력해주세요...'))
# print(userAge, type(userAge), bool(userAge)) # 28 'int'> True
# print(userAge, '=>출생년도', 2022-userAge)




# 퀴즈 : 2개의 숫자값을 입력받은 후 사칙 연산을 수행하여라
# '''
# 첫번째 숫자를 입력하세요... 10
# 두번째 숫자를 입력하세요... 20
# ---------
# 10 + 20 = ?
# 10 - 20 = ?
# 10 * 20 = ?
# 10 / 20 = ?
# '''
#
# n1 = int(input('첫번째 숫자를 입력하세요...'))
# n2 = int(input('두번째 숫자를 입력하세요...'))
#
# print(n1, '+', n2, '=' , (n1 + n2))
# print(n1, '-', n2, '=' , (n1 - n2))
# print(n1, '*', n2, '=' , (n1 * n2))
# print(n1, '/', n2, '=' , (n1 / n2))


# 문자열 더해서 






