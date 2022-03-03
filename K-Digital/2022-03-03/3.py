# 자료형의 각 요소 값을 순차적으로 출력
# for 인덱스변수 in 리스트,문자열,튜플:
#   명령문

# 리스트안의 요소를 세로로 출력하기
mylist = ['구로동', '신림동', '서초동', '역삼동']
for item in mylist:
    print(item)


print('='*50)
# while 문을 이용해서 세로로 출력
i = 0
while i<len(mylist):
    print(mylist[i])
    i+=1

print('='*50)
# 문자열을 세로롤 출력하기
txt = '가나다라마바사아'
count = 1
for i in txt:
    print(f' { count } : { i }')
    count += 1 # 증감
print('='*50)

# while 문을 이용해서 세로로 출력
i=0
while i<len(txt):
    print(f'{ i+1 } : {txt[i]}')
    i += 1

# 퀴즈 : 다음 리스트에서 60점이 넘으면 합격을 출력하고 전체 리스트의 평균, 합 출력하기
# for i in  +if 문

print('='*50)

math_list = [30, 55, 66, 100, 70]
tot = 0
for i in math_list:
    tot += i
    if i >= 60:
        print(f'{ i } => 합격 ')
    else :
        print(f'{ i } => 불합격 ')

print(f'총점 => {tot} 평균 => {tot/len(math_list):.2f}')


print('='*50)

# for 를 이용한 딕셔너리 요소 출력
# for 키변수 in 딕셔너리:
#   명령문 : 딕셔너리 변수[키변수]


# 아래의 딕셔너리를 키 => 값 형태로 세로로 출력하여라
myDict = {1:'일', 100:'백', 50:'오십', 1000:'천'}
# 딕셔너리변수[키] => 값
print(myDict[1000]) # 천
print('='*50)
for key in myDict:
    print(key, ' => ', myDict[key])
# 1  =>  일
# 100  =>  백
# 50  =>  오십
# 1000  =>  천





# 다중 리스트와 for
# 리스트안에 삽입되어 있는 리스트의 갯수가 같아야 한다.
# for (i, j...) in 다중리스트:
#   명령문

print('='*50)
# 3*2
listMulti1 = [[1, 2],
              ['a', 'b'],
              ['홍길동', '춘향이']]

# 다중 리스트(중첩 리스트) 안에서의 개별 인덱스
print(listMulti1[0]) # [1, 2]
print(listMulti1[1]) # ['a', 'b']
print(listMulti1[2][1]) # 춘향이


print('='*50 )

for ( i, j) in listMulti1:
    print(f' i = {i} , j = {j}')


# 퀴즈 : 학생이름, 국어, 영어, 수학 으로 구성된
# 2차원 리스트를 생성한다.
# 출력형식은 아래와 같이 한다.
'''
학생이름  국어  영어  수학  합계  평균
김태희     30   40   100   ?     ?
...

'''

'''
stGradeList = [['김태희', 30, 50, 55],
               ['신민아', 50, 90, 80],
               ['박지민', 50, 90, 40],
               ['김소희', 60, 50, 56],
               ['윤준희', 90, 88, 66]]

'''
print('='*50)

stGradeList = [['김태희', 30, 50, 55],
               ['신민아', 50, 90, 80],
               ['박지민', 50, 90, 40],
               ['김소희', 60, 50, 56],
               ['윤준희', 90, 88, 66]]
print('학생이름 국어 영어 수학   합계 평균')
for (student, kor, eng, math) in stGradeList:
    tot = kor + eng + math # 합계
    print(f'{student}  {kor}  {eng}  {math}    {tot}  {tot/3:.2f}')

print('='*50)
# # 퀴즈 1
# # 다음 2차원 리스트를 생성하고 결과와 같이 for...in 문을 이용하여 출력하여라
# employees = [
#                 ['김수철', '서울', 25, '남', '총무부'],
#                 ['고길동', '부산', 33, '남', '회계부'],
#                 ['최미나', '대전', 22, '여', '기획부'],
#                 ['은지원', '서울', 44, '남', '영업부'],
#                 ['김영탁', '울산', 36, '남', '영업부'],
#                 ['마동탁', '대구', 50, '남', '기획부'],
#                 ['이은미', '창원', 42, '여', '총무부']
#               ]
# print('-'*50)
# print('사원명  출신지  나이  성별  부서')
# print('-'*50)
# for (a, b, c, d, e) in employees:
#     # if a[0] == '김': # 3번답
#     #   print(f'{a}   {b}   {c}   {d}   {e}') # 1번 답
#     # if d == '남': # 2번 문제 식
#     #     print(f'{a}  {b}  {c}  {d}  {e}') # 2번 답



# # 결과 =>
#    ----------------------------------------
#      사원명     출신지     나이     성별     부서
#    ----------------------------------------
#      김수철     서울     25     남     총무부
#      고길동     부산     33     남     회계부
#      최미나     대전     22     여     기획부
#      은지원     서울     44     남     영업부
#      김영탁     울산     36     남     영업부
#      마동탁     대구     50     남     기획부
#      이은미     창원     42     여     총무부



# 퀴즈2
# 위의 리스트에서 남자 사원 목록만 출력하여라
# 결과 =>
#    ----------------------------------------
#      사원명     출신지     나이     성별     부서
#    ----------------------------------------
#      김수철     서울     25     남     총무부
#      고길동     부산     33     남     회계부
#      은지원     서울     44     남     영업부
#      김영탁     울산     36     남     영업부
#      마동탁     대구     50     남     기획부


# 퀴즈3
# 퀴즈 1의 리스트에서 성이 '김'인 사원 목록만 출력하여라
# 결과 =>
#    ----------------------------------------
#      사원명     출신지     나이     성별     부서
#    ----------------------------------------
#      김수철     서울     25     남     총무부
#      김영탁     울산     36     남     영업부




employees = [
                ['김수철', '서울', 25, '남', '총무부'],
                ['고길동', '부산', 33, '남', '회계부'],
                ['최미나', '대전', 22, '여', '기획부'],
                ['은지원', '서울', 44, '남', '영업부'],
                ['김영탁', '울산', 36, '남', '영업부'],
                ['마동탁', '대구', 50, '남', '기획부'],
                ['이은미', '창원', 42, '여', '총무부']
              ]
print('\n\n 결과1 => ')
print('\t'+'-'*50)
print(f' \t 사원명 \t 출신지 \t 나이 \t 성별 \t   부서 ')
print('\t'+'-'*50)
for (name, homtown, age, gender, part) in employees:
    print(f' \t {name} \t {homtown} \t\t {age} \t {gender} \t {part} ')


print('\n\n 결과2 => ')
print('\t'+'-'*50)
print(f' \t 사원명 \t 출신지 \t 나이 \t 성별 \t   부서 ')
print('\t'+'-'*50)
for (name, homtown, age, gender, part) in employees:
    if gender == '남':
        print(f' \t {name} \t {homtown} \t\t {age} \t {gender} \t {part} ')



print('\n\n 결과3 => ')
print('\t'+'-'*50)
print(f' \t 사원명 \t 출신지 \t 나이 \t 성별 \t   부서 ')
print('\t'+'-'*50)
for (name, homtown, age, gender, part) in employees:
    if name[0] == '김':
        print(f' \t {name} \t {homtown} \t\t {age} \t {gender} \t {part} ')




# range(start, end , step)
# start~ (end-1)까지 step만큼 차례대로 숫자 생성
# range 객체로 생성되므로
# 실제 출력을 확인하려면 리스트, 튜플, 집합 형태로 자료형 변경

print('='*50)
print(range(1, 5, 10))
print(list(range(1, 5, 10)))
print(tuple(range(1, 5, 10)))



# range(start, end , step)
# start~ (end-1)까지 step만큼 차례대로 숫자 생성
# range 객체로 생성되므로
# 실제 출력을 확인하려면 리스트, 튜플, 집합 형태로 자료형 변경

print('='*50)
print(range(1, 10)) # range(1, 10)
print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(range(1, 10))) # (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,50,2)))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]


print('='*50)
print(range(1, 10)) # range(1, 10)
print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(range(1, 10))) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,50,5))) # [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]


# for 문과 range
# for 인덱스변수 in range(start,end,step):
#   명령문

print('='*50)
# 1~10 까지 출력하기
for i in range(1,11):
    print(i, end= ' ')


print('='*50)
# 1~10까지 홀수만 출력하기
for i in range(1,11,2):
    print(i, end=' ')






