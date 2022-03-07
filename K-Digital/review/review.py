#
# 파이썬 작업환경 구축 : 아나콘다 + 파이참
# 주석
# 출력문 - print()
# 변수
# 자료형 - 숫자형(정수, 실수), 논리형(True, False), 문자열
# 연산자 - 산술, 대입, 논리, 관계(비교)
# 입력문 - input()
# 문자열 연산자 : +, *
# 문자열 인덱싱
# 문자열 슬라이싱
# 포맷팅 - %서식자, format(), f포맷팅
# 문자열 함수 - count(), replace() ...
#
# ===============================
# 집합형 자료형
# 리스트 [] => CRUD, 인덱싱, 슬라이싱, +, *
# 튜플 () => CRU, 인덱싱, 슬라이싱, +, *
# 딕셔너리 {키:값...} => CRUD, 키인덱싱
# 집합 {} => CRUD, &, -, |, ^
# 캐스팅 : list(), tuple(), dict(), enumerate(), split(), str(), ' '.join()
#
# ===============================
# 제어문 - 조건문, 반복문
# if, if~else, if~elif~else
# True/False 가 되는 값
# while ~
# for ... in 리스트/문자열/튜플
# for ... in range(start, end, step)
# pass
# continue
# break
#
# ===============================
#
# 리스트 for
# 함수 => 인자(Parameter, auguments, 전달변수) , return
# 함수 ( 인자 X, return X)
# 함수 ( 인자 O, return X)
# 함수 ( 인자 X, return O)
# 함수 ( 인자 O, return O)
# 함수 ( 인자=값....)
# 함수 ( 인자, 인자=값....)
# 함수 ( *args ) => 입력값이 튜플로
# 함수 ( **kwargs ) => 입력값이 딕셔너리로
#
#
#
# # 두번째 방법 - map()+함수
#
# # 리스트 각각에 대한 결과값을 리턴하는 함수 정의
# # 입력 x 에 대한 제곱값을 리턴하는 함수 정의
# def powerNum(x):
#     return x**2
#
# # list(map(정의된함수나 lambda함수, 데이타(리스트,튜플)))
# dataList = [1,2,3,4]
# print(dataList, ' => ', map(powerNum, dataList))
# # [1, 2, 3, 4]  =>  <map object at 0x0000026B859E2100>
# print(dataList, ' => ', list(map(powerNum, dataList)))
# # [1, 2, 3, 4]  =>  [1, 4, 9, 16]
#
#
#
#
## random 난수 함수들
# 외장모듈 필요
# import random
# random.randint(start, end)
# : start~end 사이의 정수 난수
# random.choice(리스트)
# : 리스트에서 랜덤하게 뽑는다.
# random.shuffle(리스트)
# : 리스트를 랜덤하게 섞는다.
#
#
#
#
# 람다함수
# filter(), lambda()
#
#
#
#
