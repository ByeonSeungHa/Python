# 튜플

# CRUD : Create Read Update(Add)
# 튜플 생성1 (초기값 지정)
# 튜플변수 = (값1, 값2...)

# 튜플 생성2 (초기값 지정)
# 튜플변수 = 값1, 값2...

# 튜플 생성3 (빈 튜플)
# 튜플변수 = ()

print('='*50)

t1 = ()
t2 = (100, 200, 300)
t3 = '가','나','다'
print(t1, type(t1), len(t1)) # () <class 'tuple'> 0
print(t2, type(t2), len(t2)) # (100, 200, 300) <class 'tuple'> 3
print(t3, type(t3), len(t3)) # ('가', '나', '다') <class 'tuple'> 3


print('='*50)

# 값이 1개인 경우의 튜플 선언
t4 = ('python') # 이건 문자열이다.
print(t4, type(t4), len(t4))

t4 = ('python',) # 이건 튜플이다.
print(t4, type(t4), len(t4))





# 튜플 인덱싱
# 튜플변수[인덱싱위치번호] , 0부터 시작
# 튜플 슬라이싱
# 튜플변수[start:end:step]

t5 = (100, 200, 300, '가', '나', '다')
print('='*50)
print(t5)
print(t5[0], t5[-1]) # 100 다
print(t5[:5], t5[3:], t5[1:3]) # (100, 200, 300, '가', '나') ('가', '나', '다') (200, 300)
print(t5[1::2]) # (200, '가', '다')


# 튜플의 값은 교체가 가능한가?
# TypeError , 내용 교체가 불가능하다.
# t5[0] = 0  # TypeError: 'tuple' object does not support item assignment
# print(t5) 에러가 뜬다.

# 튜플은 값을 새로 추가할 수 있는가?
# 튜플변수 += (값1,)
# 한개 추가시에는 쉼표(,) 주의
# 튜플변수 += (값1, 값2...)
t6 = ()
print(f' t6 = {t6} ') # t6 = ()
t6 += (100,)
print(f' t6 = {t6} ') #  t6 = (100,)
t6 += (500,)
print(f' t6 = {t6} ') # t6 = (100, 500)
t6 += ( 'python', 'django')
print(f' t6 = {t6} ') # t6 = (100, 500, 'python', 'django')


# 튜플의 값은 삭제가 가능한가?
# 튜플 요소 각각의 값 삭제는 불가능
# 튜플변수 전체 삭제는 가능
# del 튜플변수
del t6
# print(f' t6 = {t6} ') # name 't6' is not defined.

# 튜플=> 리스트 : list(튜플변수나 값)

t7 = (100, 200, 300, '가', '나', '다')
print('-'*50)
print(t7, type(t7)) # (100, 200, 300, '가', '나', '다') <class 'tuple'>
# 튜플 => 리스트 형변환
data = list(t7)
print(data, type(data)) # [100, 200, 300, '가', '나', '다'] <class 'list'>

# 퀴즈
# 다음 튜플 데이터를 리스트 데이터로 변환한 후에
# 'fun-coding0' 데이터를 첫번째에 추가하고,
#  다시 튜플 데이터로 변환하여라.

# 튜플 선언
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
# 결과
# step1 => ('fun-coding1', 'fun-coding2', 'fun-coding3')
# step2 => ('fun-coding0', 'fun-coding1', 'fun-coding2', 'fun-coding3')

tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
print(f' step1 => {tupledata} ')

# 리스트로 변환하고 첫번째 위치에 삽입
temp = list(tupledata)
temp.insert(0, 'fun-coding0')
print(temp) # ['fun-coding0', 'fun-coding1', 'fun-coding2', 'fun-coding3']

# 튜프 => 리스트 list(튜플)
# 리스트 => 튜플 tuple(리스트)
tupledata = tuple(temp)
print(f' step2 => {tupledata} ')
# step2 => ('fun-coding0', 'fun-coding1', 'fun-coding2', 'fun-coding3')










