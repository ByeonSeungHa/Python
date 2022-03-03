# 집합 (set)

# 집합의 생성
# 집합변수 = set(리스트/문자열/튜플)
# 집합변수 = { 값1, 값2 .... }
s1 = set([ 100, 200, 300 ])
s2 = set( (5, 4, 3, 2, 1,) )
s3 = set('도레미파솔')

print(s1, type(s1)) # {200, 100, 300} <class 'set'>
print(s2, type(s2)) # {1, 2, 3, 4, 5} <class 'set'>
print(s3, type(s3)) # {'레', '파', '솔', '미', '도'} <class 'set'>

# 비어있는 집합
s4 = set()
print(s4 , type(s4)) # set() <class 'set'>

# 순서가 없다. 랜덤하게 출력된다.
# 인덱싱이 불가능하다. 슬라이싱 불가능하다.
# 중복값을 허용할까요? => 1개만 표시
s5 = { 1,2,3,1,1,2,100}
print(s5, type(s5)) # {1, 2, 3, 100} <class 'set'>

# 집합의 요소 추가
# 집합변수.add(값)
# 집합변수.update([값1, 값2...])

# 집합의 요소 삭제
# 집합변수.remove(값)

s6 = set()
print(s6, len(s6)) # set() 0
s6.add('python')
s6.add('java')
s6.add('C')
print(s6, len(s6)) # {'C', 'python', 'java'} 3
s6.update(['ai', 'db', 'pandas'])
print(s6,len(s6)) # {'C', 'db', 'pandas', 'ai', 'python', 'java'} 6

# 값으로 삭제
s6.remove('C')
print(s6, len(s6)) # {'db', 'java', 'pandas', 'ai', 'python'} 5
s6.pop()
s6.pop()
print(s6, len(s6)) # {'python', 'ai', 'pandas'} 3


# 집합 합치기 = 합집합
# 집합변수3 = 집합변수1|집합변수2
# 집합변수3 = 집합변수1.union(집합변수2)

# 차집합
# 집합변수3 = 집합변수1-집합변수2
# 집합변수3 = 집합변수1.difference(집합변수2)


# 교집합
# 집합변수3 = 집합변수1&집합변수2
# 집합변수3 = 집합변수1.intersection(집합변수2)

# 대칭차집합 = 합집합-교집합
# 집합변수3 = 집합변수1^집합변수2
# 집합변수3 = 집합변수1.symmetric_difference(집합변수2)
setA = {'호랑이', '토끼', '돼지'}
setB = {'사자','토끼','돼지','펭귄', '여우'}
print(f' 합집합 = {setA|setB} {setA.union(setB)}')
# {'토끼', '호랑이', '여우', '펭귄', '돼지', '사자'} {'토끼', '호랑이', '여우', '펭귄', '돼지', '사자'}
print(f' 차집합 = {setA-setB} {setA.difference(setB)}')
# {'호랑이'} {'호랑이'}
print(f' 교집합 = {setA&setB} {setA.intersection(setB)}')
# {'토끼', '돼지'} {'토끼', '돼지'}
print(f' 대칭차집합 = {setA^setB} {setA.symmetric_difference(setB)}')
# {'펭귄', '여우', '호랑이', '사자'} {'펭귄', '여우', '호랑이', '사자'}

# 캐스팅
# 집합 => 리스트 list()
# 집합 => 튜플 tuple()
# 집합 => 딕셔너리 dict(enumerate())
# 집합 => 문자열 str() , '구분자'.join()

setC ={'펭귄', '호랑이',' 사자','토끼','여우','돼지'}
listC = list(setC)
tupleC = tuple(setC)
dictC = dict(enumerate(setC))
print('='*50)
print(setC , type(setC)) # {'호랑이', '토끼', ' 사자', '펭귄', '돼지', '여우'} <class 'set'>
print(setC,type(listC)) # {'호랑이', '토끼', ' 사자', '펭귄', '돼지', '여우'} <class 'list'>
print(tupleC, type(tupleC)) # ('펭귄', '토끼', ' 사자', '돼지', '호랑이', '여우') <class 'tuple'>
print(dictC, type(dictC)) # {0: '펭귄', 1: '토끼', 2: ' 사자', 3: '돼지', 4: '호랑이', 5: '여우'} <class 'dict'>

txtC1 = str(setC)
txtC2 = '=='.join(setC)
print(txtC1, type(txtC1)) # {'펭귄', '토끼', '돼지', '여우', ' 사자', '호랑이'} <class 'str'>
print(txtC1[2]) # 펭
print(txtC2, type(txtC2)) # 펭귄==토끼==돼지==여우== 사자==호랑이 <class 'str'>

print('='*50)
# 퀴즈1
# number_list에서 중복 숫자를 제거한 후 리스트를 만들어서 출력하여라.
# number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
# 결과 => [ .... ]
number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
number_list1 = list(set(number_list))
print('결과 =>',number_list1)

# 퀴즈2
# 두 집합의 중복 값으로 리스트를 생성하여라.
# set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
# set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
# 결과 => [ .... ]
set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
set3 = (f'{list(set1&set2)} ')
print(set3)


# 퀴즈3
# 퀴즈 2의 결과 리스트를 다음과 같이 구분자 '/'를 이용한 문자열로 출력하여라.
# 결과 =>  ? / ? / ....

set4 = ' / '.join(set3)
print('결과 =>',set4)


# 연산자 정리
# 튜플, 리스트 => +,*
# 집합 => |, &,-,^

txt1 = 'hello '
txt2 = 'python'
print(txt1 + txt2, ' / ', txt1*3) # hello python  /  hello hello hello
t1 = ( 1,2,3,)
t2 = ( 100,200,300)
print(t1 + t2, ' / ', t1*3) # (1, 2, 3, 100, 200, 300)  /  (1, 2, 3, 1, 2, 3, 1, 2, 3)


# 인덱싱 정리
# 인덱싱, 슬라이싱 => 리스트, 튜플, 문자열
# 키인덱싱 => 딕셔너리
# 인덱싱 X, 슬라이싱 X => 집합

# 값 변경 => 리스트, 딕셔너리
# 값 변경 X => 튜플, 집합

# 아이템 추가 => 리스트, 튜플, 딕셔너리, 집합

# 아이템 삭제 => 리스트, 딕셔너리, 집합
# 아이템 삭제 X => 튜플


# 문자열 => 리스트 list(), split() => 공백을 기준으로 문자열 분리 => 리스트
txt3 = 'abcdefg'
txt4 = 'a b c d e f g'
result1 = list(txt3)
result2 = list(txt4)
print(result1, len(result1)) # ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 7
print(result2, len(result2)) # ['a', ' ', 'b', ' ', 'c', ' ', 'd', ' ', 'e', ' ', 'f', ' ', 'g'] 13
result3 = txt3.split()
result4 = txt4.split()
print(result3, len(result3)) # ['abcdefg'] 1
print(result4, len(result4)) # ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 7



# =====================================================================================

# 집합형 자료형
# 리스트 [] => CRUD, 인덱싱, 슬라이싱, +, *
# 튜플 () => CRU, 인덱싱, 슬라이싱, +, *
# 딕셔너리{키:값...} => CRUD, 키인덱싱
# 집합{} => CRUD, &, -, |, ^
# 캐스팅 : list(), tuple(), dict(), enumerate(),split(), str(), ''.join()






