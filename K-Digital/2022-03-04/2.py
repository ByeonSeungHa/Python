# 사용자정의함수 정의
# 함수정의 문법
'''
def 함수이름(인자1, 인자2...):
    명령문
    ...
    return 문
'''

# 호출시
# 함수명(값1, 값2 ...)


# 함수 정의 1
# 인자도 없고 return문도 없음
'''
# 정의 
def 함수이름():
    명령문
    ...

# 호출 
함수이름()   
'''


# Hello world를 n번 출력하는 함수 정의
def hello():
    n = 5
    for i in range(n):
        print(f' {i} => Hello world')
    print('=' * 50)


# 함수 호출1
hello()
# 함수 호출2
hello()

# 함수 정의 2
# 인자가 있다. return이 없다.
# 인자 = 파라미터 = 아규먼트(arguments) = 전달변수
'''
def 함수명(인자1,인자2..):
    인자가 있는 명령문

# 호출
# 함수명(값1, 값2...)
'''


# 메세지를 n번 출력하는 함수 정의
# 메세지랑 n은 인자로 활용 => 함수로 값을 전달한다.

def hello2(message, n):
    for i in range(n):
        print(f' {i} => {message}')
    print('=' * 50)


hello2('오늘도 좋은하루!!!', 3)
hello2('Good night', 5)

# 함수 정의 3
# 인자가 없다. return이 있다
# return 문은 함수를 탈출하는 용도로도 사용.
# return 문 아래의 명령은 실행이 되지 않는다.
'''
def 함수명():
    명령문...
    return 결과값/수식/명령문

# 호출 
함수이름()       
'''


# 이름값을 입력받아서 인사말을 생성하는 함수 정의
def hello3():
    userName = input('당신의 이름은?...')
    message = userName + ' 님 환영합니다.'
    return

print('=' * 50)


# 함수호출1
# 출력문안에 함수 호출 한 경우
# print(hello3())

# 함수호출2 - 변수값으로 함수를 호출
# result = hello3()
# print(result)

# 함수 정의 4
# 인자가 있다. return이 있다
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값/수식/명령문


# 호출
# 함수명(값1, 값2...)
'''


# n~m 까지의 합을 구하는 함수 정의
# n, m 은 인자로 전달
# n~m 까지의 합 은 함수의 최종값으로 return 받는다

def sumNM(n, m):
    tot = 0
    for i in range(n, m + 1):
        tot += i
    return tot


print(' 1~100 까지의 합은? ', sumNM(1, 100))
print(f' 51~80 까지의 합은? {sumNM(51, 80)}')


# 두수의 곱이나 두수의 합을 구하는 함수 정의
# calc( x, y, 연산자) 호출
# 연산자에 따라 결과 형태가 다르게 한다.
# if, return 문

def calc(x, y, op):
    if op == '+':
        return f' {x} + {y} = {x + y}'
    elif op == '*':
        return f' {x} X {y} = {x * y}'
    else:
        return '계산 불가'


print(calc(100, 56, '+'))
print(calc(100, 56, '*'))
print(calc(100, 56, '#'))


# 퀴즈
# 출생년도에 따른 띠를 구하는 함수 정의
# 출생년도%12 나머지 결과가  animalList의 인덱스 즉 animalList[출생년도%12]
# animalList = ['원숭이띠', '닭띠', '개띠', '돼지띠', '쥐띠', '소띠', '범띠', '토끼띠', '용띠', '뱀띠', '말띠', '양띠']
# print(2022%12)
# 함수 호출은
# animal(출생년도)
# 태어난 년도는 ???? 이고 ??? 띠입니다.

# 인자 O, return O
def animal(year):
    animalList = ['원숭이띠', '닭띠', '개띠', '돼지띠', '쥐띠', '소띠', '범띠', '토끼띠', '용띠', '뱀띠', '말띠', '양띠']
    index = year % 12
    return f"태어난 년도는 {year} 이고, {animalList[index]} 입니다."


print('=' * 50)
print(animal(2022))


# 인자 O, return X
def animal2(y):
    animalList = ['원숭이띠', '닭띠', '개띠', '돼지띠', '쥐띠', '소띠', '범띠', '토끼띠', '용띠', '뱀띠', '말띠', '양띠']
    print(f'태어난 년도는 {y} 이고 {animalList[y % 12]}입니다')


print('=' * 50)
animal2(2022)

# 함수 정의 5
# 인자가 있다. return 값이 다중인 경우
# 다중 return 값인 경우 자료형은 튜플
# (결과값1, 결과값2...)
# 각각의 결과값은 인덱싱 으로 접근할 수 있다.
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 값1/수식1 , 값2/수식2 ...

# 호출
# 함수명(값1, 값2...)

'''


# x,y 값을 전달해서 사칙연산 결과를 구하는 함수 정의
def calculator(x, y):
    return x + y, x - y, x * y, x / y


print('=' * 50)
result = calculator(10, 3)
print(result, type(result))
print('두수 덧셈 결과는? ', calculator(10, 3)[0])
print('두수 곱셈 결과는? ', calculator(10, 3)[2])

# 함수 정의 6
# 인자의 초기값 설정 (모든 인자의 초기값이 있는 경우)
'''
def 함수명(인자1=값1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문

# 호출
# 함수명()
# 함수명(값1)
# 함수명(값1, 값2)
# 두수의 합 리턴. 초기값 있음
'''


# 데이타 전달 함수 정의
# 전달값이 없다면 없음으로 표시

# 인자 O, return X
def sample(x='없음', y='없음'):
    print(f' x = {x}')
    print(f' y = {y}')
    print('=' * 50)


sample('홍길동', '고길동')
sample('홍길동')
sample()

# 함수 정의 7
# 인자의 초기값 설정 (인자의 일부만 초기값이 있는 경우)
# 주의 사항은 마지막 인자부터 초기값이 있어야 한다.
# def 함수명(인자1=값2, 인자2): 에러 발생
'''

def 함수명(인자1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문

# 호출
# 함수명(값1)
# 함수명(값1, 값2)
'''

# 데이타 전달 함수 정의
# 전달값이 없다면 없음으로 표시
# 인자 O, return X
print('\n' * 5)


def sample2(x, y='없음'):
    # def sample2(x ='없음', y): # SyntaxError
    print(f' x = {x}')
    print(f' y = {y}')
    print('=' * 50)


sample2('홍길동', '고길동')
sample2('홍길동')


# sample2() #TypeError

# 퀴즈
# 아래의 함수를 호출했을때 결과값이 출력되도록 함수를 정의하여라.
# sumNumber() => 0
# sumNumber(1,2) => 1+2=?
# sumNumber(4,5,6) => 4+5+6=?
# sumNumber(4,5,6,10) => 4+5+6+10=?

# 인자 O, return O
def sumNumber(a=0, b=0, c=0, d=0):
    return f' {a} + {b} + {c} + {d} = {a + b + c + d}'


print(f'sumNumber() => {sumNumber()}')
print(f'sumNumber(1,2) => {sumNumber(1, 2)}')
print(f'sumNumber(4,5,6) => {sumNumber(4, 5, 6)}')
print(f'sumNumber(4,5,6,10) => {sumNumber(4, 5, 6, 10)}')


def sumNumber2(a=0, b=0, c=0, d=0):
    result = [a, b, c, d]  # 리스트화
    result2 = []  # 0을 제외한 숫자로 리스트
    tot = a + b + c + d
    for i in result:
        # 0이 아닌 경우 문자열로 변경해서 리스트에 추가
        if i != 0:
            result2.append(str(i))  # 숫자를 문자로 만들어 리스트 추가

    if tot != 0:
        return (' + '.join(result2)) + ' = ' + str(a + b + c + d)
    else:
        return 0


print('=' * 50)
print(f'sumNumber() => {sumNumber2()}')
print(f'sumNumber(1,2) => {sumNumber2(1, 2)}')
print(f'sumNumber(4,5,6) => {sumNumber2(4, 5, 6)}')
print(f'sumNumber(4,5,6,10) => {sumNumber2(4, 5, 6, 10)}')

# 함수 정의 8
# 가변인자인 경우 : 인자의 갯수가 정해지지 않는 경우
# *args => arguments
# 인자가 args 튜플로 반환
'''
def 함수명(*args):
    args에 관련된 명령문...
    return 값/변수/수식/명령문

# 호출
# 함수명(값1)
# 함수명(값1, 값2)
# 함수명(값1, 값2, 값3 ...)

'''


# 데이타를 무작위로 전달한 후 출력하는 함수 정의
def samplePrint(*args):
    print('=' * 50)
    print(args, type(args))


samplePrint(100, 200, 300)
samplePrint('Phython', True, 3.14, 78, 1000)
samplePrint()


# 함수에 전달되는 값을 모두 합하여라
# sumNumberA() => 0
# sumNumberA(1,2) => 1+2=?
# sumNumberA(4,5,6,10) => 4+5+6+10=?

def sumNumberA(*args):
    # print('\n 함수호출')
    tot = 0
    for i in args:
        # print(i)
        tot += i
    return tot


print(f'sumNumberA(4,5,6,10) = {sumNumberA(4, 5, 6, 10)}')
print(f'sumNumberA(1,2) = {sumNumberA(1, 2)}')

# 가변인자 퀴즈
# 함수의 전달값을 모두 곱한 후 결과를 출력하여라
# mulNumber() # 인자값이 없다
# mulNumber(1,2) # 1X2 =2
# mulNumber(4,5,6) # 4x5x6 = 120
# mulNumber(4,5,6,10) # 4x5x6x10x50 = 60000

def mulNumber(*args):
    print('함수 호출')
    result = 1
    for i in args:
        result *= i
    if len(args) != 0:
        print(f'{args} 의 모든 수의 곱은? {result}')
    else:
        print('인자값이 없다')
mulNumber(4,5,6,10,50)
mulNumber(1,2)
mulNumber()

# 가변인자, return
def mulNumber2(*args):
    if len(args) != 0:
        # 전체 곱구하기
        result = 1
        for i in args:
            result *= i
        # 문자열로 구성된 리스트로 변경
        txt  = 'X'.join([str(i) for i in args])
        return txt + ' = ' + str(result)
    else :
        return '인자값이 없다'
print('='*50)
print(mulNumber2(4,5,6,10,50))
print(mulNumber2(1,2))
print(mulNumber2())


    # if len(args) != 0:
    #     print(f'{args} 의 모든 수의 곱은? {result}')
    # else:
    #     print('인자값이 없다')


# 함수 정의 9
# 일반인자랑 가변인자랑 함께 있는 경우
# 주의 사항: 일반 인자는 앞쪽으로 배치. 가변 인자 *args는 뒷편에 배치
'''
def 함수명(인자, *args):
    인자와 args를 이용한 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(인자값, 가변값1)
# 함수명(인자값, 가변값1, 가변값2...)

# 학생명(일반인자), 과목점수(가변인자)
# 함수 정의 후 출력
# 과목점수가 없는 경우는 수강 과목이 없다 는 메세지 출력

def student(stdName, *args):
# def student(*args, stdName):
    print(f' 학생명 => {stdName}')
    # if args != 0 :
    if args :
        print(f' 점수 => {args}')
    else:
        print('수강 과목이 없다')
    print('=' * 50)


student('홍길동', 77, 88)
student('고길동', 45, 25, 77, 88, 100)
student('박길동')


# 퀴즈
# 산술 연산자의 기호에 따라 곱한값이나 더한값이 출력되도록 하여라
# 함수 호출1
# calChoice('*', 20,30)
# 계산결과 = 곱 : 600
# 함수 호출2
# calChoice('*', 20,30,50)
# 계산결과 = 곱 : ?
# 함수 호출3
# calChoice('+', 20,30,50)
# 계산결과 = 합 : 100
# +, - 연산자가 아니라면 메세지 출력 => 계산 오류 등

# sum(리스트/튜플) => 리스트의 총합
# min(리스트/튜플) => 가장작은 숫자
# max(리스트/튜플) => 가장큰숫자
mylist = [ 10, 45, 100, -90]
print(sum(mylist), min(mylist), max(mylist))
# 65 -90 100


def calChoice(op, *args):
    if op == '+':
        return f'계산결과 = 합 : {sum(args)}'
    elif op == '*':
        result = 1
        for i in args:
            result *= i
        return f'계산결과 = 곱 : {result}'
    else:
        return '계산 오류'

print(calChoice('+', 20, 30, 50))
print(calChoice('*', 20, 30))
print(calChoice('/', 10, 20))


# 함수 정의 11
# 초기값이 있는 딕셔너리 가변인자 **kwargs
# keyword argument
# 가변인자는 키=값
# 결과 데이터형이 딕셔너리

'''
def 함수명(**kwargs):
    # 초기값 지정
    kwargs[키값] = 값
    kwargs를 명령문...
    return 값/변수/수식/명령문
# 호출
# 함수명(키1=값1)
# 함수명(키1=값1, 키2=값3 ...)
'''


# 학생 정보를 딕셔너리 구조로 생성하는 함수 정의
def stdInfo(**kwargs):
    print('\n 함수 호출')
    print(kwargs, type(kwargs))
    for key in kwargs:
        print(f' {key} => {kwargs[key]}')

# 함수호출
stdInfo(stdName='김철수', age=28, gender='남')
stdInfo(stdName='이영자', gender='여', addr='부산', job='개그맨')

# 함수 정의 11
# 초기값이 있는 딕셔너리 가변인자 **kwargs
# 가변인자는 키=값
# 결과 데이터형이 딕셔너리

'''
def 함수명(**kwargs):
    # 초기값 지정
    kwargs[키값] = 값
    kwargs를 명령문...
    return 값/변수/수식/명령문
# 호출
# 함수명(키1=값1)
# 함수명(키1=값1, 키2=값3 ...)
'''

# 주소록 스타일 함수 정의
# 가변인자 딕셔너리 함수 정의
def makeAddr(**kwargs):
    # 전달값에 nation 키가 없다면 초기값 지정
    if 'nation' not in kwargs:
        kwargs['nation'] = '한국'
    print('='*50)
    for key in kwargs:
        print(f' {key} => {kwargs[key]}')

# 함수 호출
makeAddr(userName='이승기', addr='서울', job='가수')
makeAddr(userName='김진수', addr='부산')
makeAddr(userName='마리아', addr='부산', nation='호주')



'''
====================================================
리스트 for
함수 = 인자(parameter, auguments, 전달변수), return
함수 (인자 x, return x)
함수 (인자 o, return x)
함수 (인자 x, return o)
함수 (인자 o, return o)
함수 (인자=값....)
함수 (인자, 인자=값....)
함수 ( *args ) # 입력값이 튜플로
함수 ( **kwargs ) => 입력값이 딕셔너리로
'''









