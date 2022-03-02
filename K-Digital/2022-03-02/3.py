# 딕셔너리
# CRUD : Create Read Update Delete
# 딕셔너리 생성 - 초기값 지정
# 딕셔너리변수 = {키1:값1, 키2:값2,...}
# 키값은 문자형, 숫자형 둘다 가능
# 딕셔너리변수 = {key1:value1, key2: value2, key3:value3.....}
# dic = {'name':'pay', 'phone':'0119993323', 'birth':'1118'}

dict1 = {} # 빈 딕셔너리
dict2 = {'a':'apple', 'b':'banana', 'c':'cat'} # 키값이 문자
dict3 = {100:'일백', 200:'이백'} # 키값이 숫자
print(dict1, type(dict), len(dict1)) # {} <class 'type'> 0
print(dict2, type(dict), len(dict2)) # {'a': 'apple', 'b': 'banana', 'c': 'cat'} <class 'type'> 3
print(dict3, type(dict), len(dict3)) # {100: '일백', 200: '이백'} <class 'type'> 2

# 딕셔너리 중복키는 가능할까요?
# 값은 같아도 되지만 키값이 중복되면 마지막 키값만 유효하다
dict4 = {'a':'apple', 'b':'banana', 'c':'cat', 'a':'apart'}
print(dict4, type(dict4), len(dict4)) # {'a': 'apart', 'b': 'banana', 'c': 'cat'} <class 'dict'> 3

# 딕셔너리 요소 조회 : 키인덱싱
# 딕셔너리변수[키값] => 해당요소의 값 표시

dict5 = {'a':'apple', 'b':'banana', 'c':'cat', 100:'일백', 200:'이백'}
print(dict5, type(dict5), len(dict5))
# {'a': 'apple', 'b': 'banana', 'c': 'cat', 100: '일백', 200: '이백'} <class 'dict'> 5
print(dict5['a'], dict5[100]) # apple 일백

# 리스트, 튜플처럼 숫자 인덱싱이 가능할까?
# KeyError : 딕셔너리는 키값으로만 호출가능, 위치를 알리는 숫자로는 인덱싱 불가능
# print(dict5[0])


# 리스트, 튜플처럼 숫자 인덱싱이 가능할까?
# KeyError : 딕셔너리는 키값으로만 호출가능. 위치를 알리는 숫자로는 인덱싱 불가능
# print(dict5[0])

# 리스트, 튜플처럼 슬라이싱이 가능할까?
# TypeError 딕셔너리는 슬라이싱이 불가능
# print(dict5[0:2])

# 딕셔너리 값 교체
# 딕셔너리[변경하려는키값] = 값

# 딕셔너리 요소 추가
# 딕셔너리변수[새키값]=값

print('='*50)

dict6 = {'a':'apple', 'b':'banana', 'c':'cat', 100:'일백', 200:'이백'}
print(dict6, type(dict6), len(dict6)) # {'a': 'apple', 'b': 'banana', 'c': 'cat', 100: '일백', 200: '이백'} <class 'dict'> 5

# 값 교체
dict6['a'] = 'app' # {'a': 'app', 'b': 'banana', 'c': 'cat', 100: '일백', 200: '이백'} 5
print(dict6, len(dict6))

# 새로운 요소 추가
dict6['d'] = 'drag'
print(dict6,len(dict6))
# {'a': 'app', 'b': 'banana', 'c': 'cat', 100: '일백', 200: '이백', 'd': 'drag'} 6

# 딕셔너리 요소 삭제
# 딕셔너리변수.clear()
# 딕셔너리변수.pop(키값)
# del 딕셔너리변수
# del 딕셔너리변수[키값
dict7 = {'a': 'app', 'b': 'banana', 'c': 'cat', 'd': 'drag'}
print('='*50)
print(dict7) # {'a': 'app', 'b': 'banana', 'c': 'cat', 'd': 'drag'}
dict7.pop('b')
print(dict7) # {'a': 'app', 'c': 'cat', 'd': 'drag'}
del dict7['d']
print(dict7) # {'a': 'app', 'c': 'cat'}
dict7.clear()
print(dict7) # {}

# 딕셔너리 함수
# 딕셔너리변수.values() : 값 만 표시
# 딕셔너리변수.keys() : 키값만 표시
# 딕셔너리변수.items() : 튜플스타일로 표시 (키, 값)...

dict8 = {'a': 'app', 'b': 'banana', 'c': 'cat', 'd': 'drag'}
print('='*50)
print(dict8, type(dict8)) # {'a': 'app', 'b': 'banana', 'c': 'cat', 'd': 'drag'} <class 'dict'>
print(dict8.values(), type(dict8.values())) # dict_values(['app', 'banana', 'cat', 'drag']) <class 'dict_values'>
print(dict8.keys(), type(dict8.keys())) # dict_keys(['a', 'b', 'c', 'd']) <class 'dict_keys'>

# 리스트 변환 list() , 튜플로 변환 tuple()
# 딕셔너리에서 값만 모아서 리스트로 생성
print(list(dict8.values()), type(list(dict8.values()))) # ['app', 'banana', 'cat', 'drag'] <class 'list'>



# 리스트 => 딕셔너리(인덱싱숫자가 키값이 된다)
# 리스트 => enumerate(리스트,문자열,튜플)
#   => dict(enumerate(리스트,문자열,튜플))
# dict()
# enumerate(리스트,문자열,튜플)
# : 리스트,문자열,튜플 같은 자료형을 enumerate 객체로 반환
# enumerate 객체의 요소는 딕셔너리 스타일. 키값은 숫자로 표시

fruitList = [ '바나나', '포도', '오렌지']
print( fruitList , type(fruitList) ) # ['바나나', '포도', '오렌지'] <class 'list'>
# print( enumerate(fruitList) ) # <enumerate object at 0x0000015694E6FA00>
temp = enumerate(fruitList)
fruitDict = dict(temp) # 딕셔너리화
print( fruitDict , type(fruitDict)) # {0: '바나나', 1: '포도', 2: '오렌지'} <class 'dict'>

# 튜플 => 딜셔너리
# dict(enumerate(튜플))
mytuple = (100,200,300)
myDict = dict(enumerate(mytuple))
print('='*50)
print(mytuple , type(mytuple)) # (100, 200, 300) <class 'tuple'>
print(myDict, type(myDict)) # {0: 100, 1: 200, 2: 300} <class 'dict'>

# 딕셔너리 값만 => 튜플 tuple(딕셔너리명.values())
# 딕셔너리 키만 => 튜플 tuple(딕셔너리명.keys())
myDict2 = {'a':'app', 'b':'banana', 'c':'cat', 'd': 'drag'}
mytupleA = tuple(myDict2.values())
mytupleB = tuple(myDict2.keys())
print(myDict2, type(myDict2)) # {'a': 'app', 'b': 'banana', 'c': 'cat', 'd': 'drag'} <class 'dict'>
print(mytupleA, type(mytupleA)) # ('app', 'banana', 'cat', 'drag') <class 'tuple'>
print(mytupleB, type(mytupleB)) # ('a', 'b', 'c', 'd') <class 'tuple'>


# 딕셔너리 => 문자열
# str(딕셔너리변수) => {...}
# 구분자.join(딕셔너리변수) => 키값으로 생성된 문자열. 키값의 대상이 문자이어야한다.
print('='*50)


myDict2 = {'a':'app', 'b':'banana', 'c':'cat', 'd': 'drag'}
myString = str(myDict2)
print(myString,type(myString)) # {'a': 'app', 'b': 'banana', 'c': 'cat', 'd': 'drag'} <class 'str'>
print(myString[0],myString[0:5], myString[-1]) # { {'a': }


# 딕셔너리에서 키값만 추출해서 문자열로 생성
myString2 = ''.join(myDict2)
myString3 = '/'.join(myString2)
print(myString2 , type(myString2 )) # abcd <class 'str'>
print(myString3 , type(myString3 )) # a/ /b/ /c/ /d <class 'str'>

# 딕셔너리에서 값만 추출해서 문자열로 생성
myString4 = ' / '.join(myDict2.values())
print(myString4, type(myString4)) # app / banana / cat / drag <class 'str'>

# 문자열 => 리스트 list()
# 문자열 => 튜플 tuple()
txt1 = "가나다라마바사"
mylist1 = list(txt1)
mytuple1 = tuple(txt1)
print(txt1 , type(txt1)) # 가나다라마바사 <class 'str'>
print(mylist1,type(mylist1)) # ['가', '나', '다', '라', '마', '바', '사'] <class 'list'>
print(mytuple1,type(mytuple1)) # ('가', '나', '다', '라', '마', '바', '사') <class 'tuple'>

# 문자열 => 딕셔너리 dict(enumerate(문자열))
mydict1 = dict(enumerate(txt1))
print(mydict1 , type(mydict1)) # {0: '가', 1: '나', 2: '다', 3: '라', 4: '마', 5: '바', 6: '사'} <class 'dict'>































