# 람다 함수
# def 로 정의하지 않다.
# 한줄로 정의한다.
'''
# 람다함수 정의
함수변수 = lambda 인자:명령

# 람다함수 호출
함수변수(인자)
'''


# 고객이름 => 인자, 함수결과 => 인자를 이용한 메세지

# 일반 함수 스타일
def message1(userName):
    return userName + '님 안녕하세요'

print(message1('홍길동'))
print(message1('이승기'))


# 람다(lambda) 함수 스타일
message2 = lambda userName:userName + '님 안녕하세요'

print(message2('홍길동2'))
print(message2('이승기2'))


print('='*50)

# 3수의 합을 구하는 함수 정의

# 일반 함수 스타일
def addNum(x, y, z):
    return f'{x} + {y} + {z} = {x+y+z}'
print(addNum(10, 20, 30))

# 람다(lambda) 함수 스타일
addNum2 = lambda x, y, z : f'{x} + {y} + {z} = {x+y+z}'

print(addNum2(10, 20, 30))

print('='*50)


# filter(함수명/lambda 함수, 리스트/튜플),
# map(함수명/lambda 함수, 리스트/튜플),
# reduce(함수명/lambda 함수, 리스트/튜플)
# 정의된 사용자정의함수, 람다함수를  리스트 데이타 각각에 적용한다.

# filter()
# filter(함수명/lambda 함수, 리스트/튜플)
# 사용할 함수는 결과값이 True/False
# 함수를 적용하여 리스트/튜플의 data에서 True 인것만 Return
# => 참인조건의 리스트만 출력

# =============================================================

# 퀴즈
# 리스트 중 짝수만 출력하기 = filter() 함수 이용
# 짝수인지 판독하는 함수 정의
# 리스트 정의
# filter() 함수 적용 => filter 객체
# filter 객체를


num_list = [10,50, 3, 11, 90, 6, 7]
# 방법1 - 일반 함수 사용

# 리스트를 입력받은 후 짝수만 추출해서 새로운 리스트로 반환
def odd1(datalist):
    resultlist = []
    for item in datalist:
        if item%2 ==0:
            resultlist.append(item)
    return resultlist
print(num_list, odd1(num_list))

# 방법2 - filter() + 일반 함수
# 짝수인지 판독하는 함수 정의
# 1개의 데이터에 적용될 함수 생성 => True 또는 False로 리턴되어야함
# 짝수이면 True를 반환하는 함수 정의
def oddNum(x):
    if x%2 == 0:
        return True
    # else :   # True만 뽑는식이라 else가 없어도 된다.
    #     return False

print(oddNum(10))
print(oddNum(1))

print('='*50)

# fillter() 함수 적용
# filter(함수명/lambda 함수, 리스트/튜플)
numList = [10, 50, 3, 11, 90, 6, 7]
print(filter(oddNum, numList)) # 필터객체 <filter object at 0x000002440F197E20>
print(numList , list(filter(oddNum, numList)))
# [10, 50, 3, 11, 90, 6, 7] [10, 50, 90, 6]

print('='*50)

# 방법3 - filter() + 람다함수
print(numList , list(filter(lambda x:x%2 ==0, numList)))

print('='*50)

# 리스트에서 양수만 출력하여라
numlist2 = [10, -90, 0, 100, 55, -1]

# 첫번째 방법 - 일반함수 이용
# 리스트를 입력받아서 양수만으로 구성된 리스트 반환
def positiveNum(datalist):
    resultlist = [] # 빈리스트 생성
    for item in datalist:
        if item>0: # 값이 0보다 그다면
            # 리스트에 추가
            resultlist.append(item)
    return resultlist

# 함수 호출
print(numlist2, positiveNum(numlist2))
# [10, -90, 0, 100, 55, -1] [10, 100, 55]


print('='*50)

# 두번째 방법 - filter() + 함수 이용

# 함수 정의 => 입력값이 양수이면 True 반환
def positiveNum2(x):
    return x>0

# filter() 함수로 호출
print(numlist2, list(filter(positiveNum2, numlist2)))
# [10, -90, 0, 100, 55, -1] [10, 100, 55]

print('='*50)

# 세번째 방법 - filter() + 람다 함수 이용
print(numlist2, list(filter(lambda x:x>0, numlist2)))

print('='*50)

# map() 함수
# map(정의된함수나 lambda함수,데이타(리스트,튜플))
# -> map오브젝트 생성
# list(map(정의된함수나 lambda함수, 데이타(리스트,튜플)))
# 데이타 요소를 정의된함수의 결과값으로 리턴한다.
# 결과값을 리스트 요소로 추가

# 리스트의 제곱을 구해서 새로운 리스트로 만들기
# [1, 2, 3, 4] => [1, 4, 9, 16]

# 첫번째 방법 - 일반함수 이용
def powerlist(datalist):
    resultlist = []
    for item in datalist:
        resultlist.append(item**2)
    return resultlist

datalist = [1, 2, 3, 4]
print(datalist, '=>', powerlist(datalist))

print('='*50)

# 두번째 방법 - map()+함수

# 리스트 각각에 대한 결과값을 리턴하는 함수 정의
# 입력 x 에 대한 제곱값을 리턴하는 함수 정의
def powerNum(x):
    return x**2

# list(map(정의된함수나 lambda함수, 데이터(라스트,튜플)))
datalist = [1, 2, 3, 4]
print(datalist, '=>', map(powerNum, datalist))
# [1, 2, 3, 4] => <map object at 0x000001C575B6BD00>
print(datalist, '=>', list(map(powerNum, datalist)))
# [1, 2, 3, 4] => [1, 4, 9, 16]

print('='*50)

# 세번째 방법 - map()+람다함수
print(datalist, '=>', list(map(lambda x:x**2, datalist)))
# [1, 2, 3, 4] => [1, 4, 9, 16]

print('='*50)

# 학생이름으로 구성된 리스트에서 학생명마다 문자열 재정의
# ['홍길동', '고길동', '박길동', '은지환', '이영순']
# 결과 => ['홍길동', '고길동', '박길동', '은지환', '이영순']

# 첫번쨰 방법 - 일반함수 이용
def namelist(datalist):
    resultlist = []
    for item in datalist:
        resultlist.append(item +'님')
    return resultlist


datalist = ['홍길동', '고길동', '박길동', '은지환', '이영순']
print(datalist, '=>', namelist(datalist))

print('='*50)
# 두번째 방법 - map()+일반함수
def nameData(x):
    return '고객' + x + '님'
datalist = ['홍길동', '고길동', '박길동', '은지환', '이영순']
print(datalist, '=>', list(map(nameData, datalist)))

print('='*50)

# 세번째 방법 - map()+람다함수
datalist = ['홍길동', '고길동', '박길동', '은지환', '이영순']
print(datalist, '=>', list(map(lambda x:'고객'+x+'님', datalist)))

print('='*50)


# random 난수 함수들
# 외장모듈 필요
# import random
# random.randint(start, end)
# : start~end 사이의 정수 난수
# random.choice(리스트)
# : 리스트에서 랜덤하게 뽑는다.
# random.shuffle(리스트)
# : 리스트를 랜덤하게 섞는다.

# 모듈 임포트
import random

# rendom.randint(start,end)
# : start~end 사이의 정수 난수
print(random.randint(1,10), random.randint(50,100), random.randint(1000,2000))

print('='*50)
# 5개만 난수
for i in range(5):
    print(f' {i+1} 번째 숫자는? {random.randint(1,10)}')


print('='*50)

# random.choice(리스트)
# : 리스트에서 랜덤하게 뽑는다.

eventlist = ['신라면 1상자', '순금 10돈', '초코파이 1상자', '파리바게트 상품권 10만원', '캠핑카']
print('이벤트 당첨 확인1 => ', random.choice(eventlist))
print('이벤트 당첨 확인2 => ', random.choice(eventlist))

print('='*50)

# random.shuffle(리스트)
# : 리스트를 랜덤하게 섞는다. 원본 리스트자체를 무작위 순으로 정리

print(eventlist)
random.shuffle(eventlist)
print(eventlist)

print('='*50)

# 학생중에서 2명을 뽑아서 청소당번을 지정하려고 한다.
# 오늘 당번 => ?, ?
# 내일 당번 => ?, ?
studentlist = ['영희', '철수', '영수', '지원']

print(studentlist)
random.shuffle(studentlist)
print('오늘 당번 =>',studentlist[:2])
random.shuffle(studentlist)
print('내일 당번 =>', studentlist[:2])


print('='*50)

# 퀴즈 : 로또번호 출력하기
# 로또 숫자는 1~36 숫자중에서 6개가 출력된도록 한다.
# 로또 숫자는 중복값이 없어야 한다.
# 함수를 이용하여라
# 출력 예시
# print(lotto()) 함수 호출시
# [10, 25, 1, 22, 12, 8]
# while() + in, not in 연산자 + random.randint()
def lotto():
    numlist = []
    while(len(numlist)<6):
        x=random.randint(1,36)
        # 리스트에 중복값이 없다면 데이터를 리스트에 추가
        if x not in numlist:
            numlist.append(x)
    return numlist
print(lotto())

print('='*50)

#range() + random.shuffle()
def lotto2():
    # 1~36까지의 리스트 생성 [1,2,3...36]
    lotto = list(range(1,37))
    # 무작위로 순서를 섞는다
    random.shuffle(lotto)
    # 6개만 반환
    return lotto[:6]
print(lotto2())

print('='*50)







