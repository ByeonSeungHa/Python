# 파이썬 제어문
# 제어문의 종류
# - 조건문 : if / if ~ else / if ~elif~else
# - 반복문 : for / while

# 파이썬 제어문의 특징 :
# {} 사용하지 않고 탭1개 나 공백4칸 으로 블록 지정
# 들여쓰기가 없는 경우 IndentationError: 에러 발생
# switch 문이 없다
# else if 대신 elif 문이 있다

# 조건문 if

# 조건문 1 - 단순 if 문
# 조건이 참(True)이면 명령문 실행
# if 조건:
#   명령문

# 변수값이 양수이면 메세지 출력
mynum = -90
# if mynum > 0: # False
#    print('양수이다')
# if 안에 실행되는 명령문이 한개인 경우에는 한줄 코딩 가능
if (mynum>0) : print('양수이다')
print('if 테스트 종료')

# id, password 가 맞으면 메세지 출력
user_id = 'python123'
user_pwd = '1234'

print('='*50)
if (user_id == 'python') and (user_pwd == '1234') :
    print('로그인 성공')
    print(f' {user_id} 님 좋은하루!!!')
print('if 테스트 종료2')


# 조건식에서 True가 되는 조건 =
# True, 0빼고 나머지숫자, 길이가 0이 아닌 (문자열, 튜플, 리스트, 딕셔너리)
# 조건식에서 False가 되는 조건
# = False, 0, '', None, [], (), {}

print('='*50)

# status = True
# status = 100 # True
# status = 0 # False
# status = -2000 # True
# status = '' # 빈문자열 False
# status = '가나다' # 문자열 True
# status = [] # 빈리스트 False
# status = [100, 200, 300] # 리스트 True

status = None # False

if status:
    print('Hello World')
print('if 테스트 종료3')

# if 문을 다중으로 사용
# # 짝수인지 홀수인지 판단 ?
# 숫자%2 == 0:

print('='*50)
n = 77
if n%2 == 0:
    print('짝수')
if n%2 != 0:
   print('홀수')

print('if 테스트 종료4')


# 조건문 2
# if 조건: - 2가지 조건이 있는 if문
#   명령문1
# else:
#   명령문2

# 짝수인지 홀수인지 메세지 출력

print('='*50)
n = 77
if n%2 == 0:
    print('짝수')

else :
    print('홀수')

print('if else 테스트 종료1')

# 퀴즈 :
# 숫자를 입력받아서 메세지를 출력하여라 (if ~ else)
# 숫자값이 3의 배수이면 3의 배수이다.
# 그렇지 않으면 3의 배수가 아니다.

'''
숫자를 입력해주세요 ? ...
3의 배수이다.
3의 배수가 아니다.
'''
# n = int(input())

# if n % 3 == 0:
#     print('3의 배수이다.')
# else:
#     print('3의 배수가 아니다.')

# 조건문 3 - 다중 if문
# if 조건1:
#   명령문1
# elif 조건2:
#   명령문2
# else:
#   명령문3

# 두수의 대소비교
# 서로같다, 크다, 작다

n1 = -50
n2 = 100

if n1 == n2:
    print(f'{n1} == {n2}')
elif n1 > n2:
    print(f'{n1} > {n2}')
else:
    print(f'{n1} < {n2}')

print('if elif 테스트 종료1')


# 퀴즈 :
# 나이를 입력받는다.
# 나이에 따라서 서로 다른 메세지 출력
'''
당신의 나이를 입력해주세요? ...
~7 : 영유아
8 ~ 13 : 초등학생
14 ~ 16 : 중학생
17 ~ 19 : 고등학생
20 ~ : 성인
'''

print('='*50)
# age = int(input('당신의 나이를 입력해주세요?'))
#
# if age <= 7:
#     print('영유아')
# # elif (age>= 8) and (age <= 13): 이렇게하면 손이 너무많이간다.
# elif age <= 13:
#     print('초등학생')
# elif age <= 16:
#     print('중학생')
# elif age <= 19:
#     print('고등학생')
# else :
#     print('성인')
#
# print('if elif 테스트 종료2')


# 조건문안에 조건문

# 아이디가 검사 => 패스워드 검사

# user_id = input('아이디 => ')
# if user_id == 'python':
#     user_pwd = input('패스워드 =>')
#     if user_pwd == '1234':
#         print('로그인 성공')
#         print(f'{user_id} 님 좋은하루!!!')
#     else :
#         print('로그인 실패')
# else:
#     print('로그인 실패')
# print('조건문안에 조건문 테스트 종료')


#  in / not in 연산자
# 아이템 in 그룹(튜플, 리스트, 문자열, 집합) => True / False
# 아이템 not in 그룹(튜플, 리스트, 문자열, 집합) => True / False

numlist = [100, 400, 'python', 'JAVA']
sample = '가나다라마바사'

print(100 in numlist) # Treu
print(100 not in numlist) # False
print('가' not in sample) # False
print('강' in sample) # False



# if문에 in/not in 연산자 사용하기
# if item in group(리스트,튜플,문자열,집합) :
#   명령문


# if item in group(리스트,튜플,문자열,집합) :
#   명령문1
# else:
#   명령문2


# if.. elif..else.. 문에 in/not in 연산자 사용하기
# if item in group(리스트,튜플,문자열,집합) :
#   명령문1
# elif item in group(리스트,튜플,문자열,집합) :
#   명령문2
# else:
#   명령문3

print('='*50)

bts = ['지민', '뷔', 'RM']
blackpink = ['지수', '제니', '로제']

# member = '지민'
# member = '쯔위'
member = '제니'
if member in bts:
    print(f' {member} => BTS ')
elif member in blackpink:
    print(f' {member} => blackpink ')
else :
    print(member)
print('if + in 연산자 테스트')

print('='*50)

# pass 키워드 이용하기
# 명령문의 일종으로 비실행
# 함수, 클래스 생성시 등록만 시킬때 사용

pocket = ['paper', 'money', 'cellphone']

if 'paper' in pocket:
    pass
elif 'money' in pocket:
    pass
else:
    print('걸어가라')


# bmi 값에 따라 다음과 같은 메세지를 출력하세요
'''
# 키를 입력해주세요... 단위 cm...175
# 체중을 입력해주세요... 단위 kg...67
# bmi = 21.8776
# 정상
'''

# bmi 공식
# k = 키(입력값) 단위 cm
# w = 체중(입력값) 단위 kg
# bmi = 체중(kg)/키(m)의제곱, 키의 단위는 미터(m)

# bmi 값에 따라 출력되는 메세지
# 고도 비만 : 35 보다 클 경우
# 중등도 비만  : 30 - 35 미만
# 경도 비만 : 25 - 30 미만
# 과체중 : 23 - 25 미만
# 정상 : 18.5 - 23 미만
# 저체중 : 18.5 미만

k = int(input('키를 입력해주세요... 단위 cm'))
print(k,'cm')
w = int(input('체중을 입력해주세요... 단위 kg'))
print(w, 'kg')
# 미터로 수정
t = k/100
bmi = w/(t**2)
print(f'bmi = {bmi:.4f}')

if bmi < 18.5:
    print('저체중')
elif bmi < 23:
    print('정상')
elif bmi < 25:
    print('과체중')
elif bmi < 30:
    print('경도 비만')
elif bmi < 35:
    print('중등도 비만')
else:
    print('고도 비만')
# tall = int(input('키를 입력해주세요...'))
# print(tall,'cm')
# weight = int(input('체중을 입력해주세요...'))
# print(weight,'kg')
# bmi = weight/((tall/100)**2)
# print(f'bmi = {bmi:.4f}')
# if bmi >35 :
#     print('고도 비만')
# elif bmi >= 30 :
#     print('중등도 비만')
# elif bmi >=25 :
#     print('경도 비만')
# elif bmi >= 23 :
#     print('과체중')
# elif bmi >= 18.5:
#     print('정상')
# else:
#     print('저체중')


# 온라인 에디터
# https://www.onlinegdb.com/online_python_compiler
