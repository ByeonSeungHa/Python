# 자료형의 종류
# 기본 자료형 - 문자열, 정수, 실수, 불린형
# **** 집합형 자료형=콜렉션 : 여러개의 구성요소로 조직화 ****
#       : 리스트 [], 튜플 (), 딕셔너리 { }, 집합{ }
# CRUD : Create Read Update Delete


# 리스트 []
# 다른 데이터형 가능
# 순차적으로 생성
# 빈 리스트, 초기값 설정 방식

# 초기값 설정 방식을 이용한 리스트 정의
# 리스트변수 = [값1, 값2...]

# 빈 리스트를 이용한 리스트 정의
# 리스트변수 = []

list1 = []
list2 = [10,20,30] # int(정수)로만 구성된 리스트
list3 = [100,3.14,'Python',True] # int(정수),float(실수),str(문자열),bool(논리)으로 구성된 리스트

print(list1, type(list1), len(list1))
print(list2, type(list2), len(list2))
print(list3, type(list3), len(list3))

# 리스트 인덱싱
# 리스트이름[숫자] : 0부터 시작, 숫자값이 -1 마지막 요소 표시
print('='*50)
print(f'{list3} => 첫번째 요소값은?{list3[0]}')
print(f'{list3} => 마지막 요소값은?{list3[3]}')
print(f'{list3} => 마지막 요소값은?{list3[-1]}')

# 리스트 슬라이싱
# 리스트이름[start:end:step]
# 리스트이름[start:end]
# 리스트이름[start:]
# 리스트이름[:end]
# 리스트이름[::step]
# 리스트이름[:] = 리스트이름[::] = 전체리스트

print('='*50)
list4 = [1,2,3,4,5,6,7,8,9]
print(list4, len(list4))
print(list4[1:3]) # [2,3]
print(list4[-5:-2]) # [5,6,7]
print(list4[:5]) # [1,2,3,4,5]
print(list4[5:]) # [6,7,8,9]
print(list4[::2]) # [1,3,5,7,9]
print(list4[1::3]) # [2,5,8]
print(list4[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1] 역순 정렬

print('='*50)

# 리스트 함수를 이용한 값 추가
# 리스트변수.append(값) : *마지막에 아이템이 추가*
# 리스트변수.insert(삽입위치, 값) : 삽입위치에 아이템이 추가

list = []
print(list) # []
list1.append('가')
print(list1) # ['가']
list1.append('나')
print(list1) # ['가', '나']
list1.insert(0, 'python') # 0 인덱스에 값 추가
print(list1) # ['python', '가', '나']
list1.insert(2,77)
print(list1) # ['python', '가', 77, '나']

# 기존 값 변경
# 리스트명[인덱스] = 새로운 값
list1[2] = 88
print(list1) # ['python', '가', 88, '나']

print('='*50)


# 리스트 삭제와 관련된 함수와 명령어
# 리스트변수.remove(값) : 값으로 삭제하기
# 리스트변수.pop() : 마지막 요소가 삭제되면서 값이 반환된다.
# 리스트변수.pop(위치값)
# : 위치에 해당하는 요소가 삭제되면서 값이 반환된다.
# 리스트변수.clear() : 리스트안의 값이 모두 삭제. 빈리스트로 된다.
# del 리스트변수 : 리스트 자체가 삭제된다.

list4 = [1,2,3,4,5,6,7,8,9]
print(list4)
list4.remove(5) # 값으로 삭제
print(list4) # [1, 2, 3, 4, 6, 7, 8, 9]
list4.pop() # 오른쪽부터 삭제
print(list4) # [1, 2, 3, 4, 6, 7, 8]
list4.pop(0) # [2, 3, 4, 6, 7, 8]
print(list4)
list4.clear() # []
print(list4)


# 여러개의 요소를 한꺼번에 리스트에 추가 싶다면?
# 리스트변수.extend([값1,값2...])

print('='*50)

list5 = [100,200,]
print(list5) # [100,200]
list5.extend([True, False])
print(list5) # [100,200,True, False]

# 중첩 리스트 구조
# 리스트안에 리스트가 있다
# 중첩리스트의 인덱싱은?
# 리스트이름[index1][index2]

# 중첩 리스트 생성1
# 초기값으로 중첩 리스트 생성
# 리스트변수 = [ [값1, 값2...],[값1, 값2...]]

print('='*50)

# 2행 2열 리스트 선언 (2,2)
list6 = [ [10,20], [100,200]] # 10 (1.1) 20 (1.2) 100 (2.1) 200 (2.2)
print(list6, len(list6)) # [[10, 20], [100, 200]] 2

# 리스트이름[index1][index2] 인덱싱
print(list6[0], list6[0][0]) # [10, 20] 10
print(list6[1], list6[1][0]) # [100, 200] 100

print('='*50)
# 길이가 다른 중첩 리스트
list7 = ['AI', 2020, [100,200,300], [True,False]]

print(list7, len(list7))
print(list7[0]) # AI
print(list7[2], list7[2][-1]) # [100, 200, 300] 300
print(list7[3], list7[-1][-1]) # [True, False] False

print('='*50)

# 아래의 리스트를 이용하여 grade 리스트를 생성하고 합계와 평균을
# 과목별로 출력한다. 평균은 소숫점 2번째 자리까지 출력한다.
# 중첩 리스트 생성2
# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성
# 1차원 리스트 정의
kor = [ 55, 66, 34, 60]
math = [ 78, 90, 45, 88]
eng = [ 56, 98, 78, 90]
# 2차원 리스트 정의
grade = [kor, math, eng]
print(grade) # [[55, 66, 34, 60], [78, 90, 45, 88], [56, 98, 78, 90]]
kor_sum = grade[0][0]+grade[0][1]+grade[0][2]+grade[0][3]
kor_avg = kor_sum/4
print(f'kor : 합계 = {kor_sum}, 평균 = {kor_avg:.2f}') # kor : 합계 = 215, 평균 = 53.75
math_sum = grade[1][0]+grade[1][1]+grade[1][2]+grade[1][3]
math_avg = math_sum/4
print(f'math : 합계 = {math_sum}, 평균 = {math_avg:.2f}') # math : 합계 = 301, 평균 = 75.25
eng_sum = grade[2][0]+grade[2][1]+grade[2][2]+grade[2][3]
eng_avg = eng_sum/4
print(f'eng : 합계 = {eng_sum}, 평균 = {eng_avg:.2f}') # eng : 합계 = 322, 평균 = 80.50
# kor : 합계 = ? , 평균 = ?
# math : 합계 = ? , 평균 = ?
# eng : 합계 = ? , 평균 = ?

# 퀴즈 1
'''
아래와 같이 리스트를 정의하고 다음과 같이 출력한다. 

foods = ['사과','망고','치즈케이크','주스']

우리집 냉장고에는?  ['사과', '망고', '치즈케이크', '주스']
동생이 사과를 먹었다 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스']
이모가 수박을 사오셨다. 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스', '수박']
동생 친구가 치즈케이크,수박을 먹었다. 
우리집 냉장고에는?  ['망고', '주스']

'''
print('='*50)

foods = ['사과','망고','치즈케이크','주스']
foods.pop(0)
print(foods)
foods.append('수박')
print(foods)
foods.pop(1)
foods.pop(2)
print(foods)

# 퀴즈2
'''
데이터를 입력받은 후 리스트에 추가하고 출력하여라 
( input() 이용 )

좋아하는 음식은? 초밥
최근 본 영화는? 알라딘
좋아하는 가수는? BTS
좋아하는 숫자? 10
최근 여행지? 부산



당신에 관한 리스트 : ['초밥', '알라딘', 'BTS', 10, '부산' ]
'''
print('='*50)

a = input()
print('좋아하는 음식은?', a[2:4])
print('최근 본 영화는?', a[8:11])
print('좋아하는 가수는?', a[15:18])
print('좋아하는 숫자', a[21:23])
print('최근 여행지', a[26:28])

# 다른식

# # yourList = []
# # yourList.append(input('좋아하는 음식은? ... '))
# # yourList.append(input('최근 본 영화는?  ... '))
# # yourList.append(input('좋아하는 가수는? ... '))
# # yourList.append(input('좋아하는 숫자? ... '))
# # yourList.append(input('최근 여행지? ... '))
# # print(f'당신에 관한 리스트 : {yourList}')
#
# food = input("좋아하는 음식은?")
# movie = input("최근 본 영화는?")
# singer = input("좋아하는 가수는?")
# num = int(input("좋아하는 숫자는?"))
# travel = input("최근 여행지는?")
#
# about_you = [food, movie, singer, num, travel]
# print("당신에 관한 리스트 :", about_you)











