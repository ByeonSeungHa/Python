# 1~100사이의 합 구하기
tot = 0
for i in range(1,101):
    print(i, end=" ")
    tot += i
print(f'\n\n 1~100까지의 합은?{tot}')



# 중첩 for 문
# 점선 출력 후 문단 3번찍기 n번 반복하기

for i in range(3):
    print('='*30)
    for j in range(5):
        print(f' {j} => Hello World')



# 2~9단 출력하기
n = 0
for i in range(2,10):
    print(f'\n {i}단')
    for j in range(1,10):
        print(f' {i} X {j} = {i*j} ')


print('='*50)

# 1~50 사이의 숫자 중에서 3, 8, 10의 배수만 출력하라
n=[]
for i in range(1,51):
    if i %3 == 0 or i%8 ==0 or i%10 ==0:
        print(i, end=' ')



# 입력 데이터로 리스트를 생성하여라
# 리스트 길이는 5개로 한다.
# mylist = []
# for i in range(5):
#     data = input('\n데이타 입력 => ')
#     mylist.append(data)
# print(f'\n\n리스트  => {mylist}')

print('='*50)

# 퀴즈1 : 별찍기
'''
*
**
***
****
*****
'''

for i in range(6): # 내가 푼식
    print(i*'*')
# print('='*10) # 다른방법 1
# for i in range(1,6):
#     print('* '*i)
#
# print('='*10) # 다른방법 2
# for i in range(5):
#     for j in range(i+1):
#         # print('*', end=' ')
#         print(j, end=' ')
#     print()

print('='*50)

# 퀴즈 2

'''
*****
****
***
**
*
'''
for i in range(5,0,-1): # 내가 푼식
    print(i*'*')
# for i in range(5, 0, -1): 다른방법
#     print()
#     for j in range(0, i):
#         print('*', end='  ')


# 리스트 for = 리스트 내포
# 리스트 안에 for 문이 내포된 형태
# 결과값으로 구성된 리스트가 생성된다.
# 리스트변수 = [ 결과값 for 명령문 ]

print('='*50)
# 다음과 같은 리스트를 만들어라
# ['col-1', 'col-2',....'col-10']
resultlist = []
for i in range(1,11):
#   resultlist.append('col-' + i) # type error
    resultlist.append('col-' + str(i))
print(resultlist)

# 리스트내포방식 이용 리스트변수 = [결과값 for 명령문]
resultlist2 = ['col-' + str(i) for i in range(1,11)] # 한줄 식
print(resultlist2)


print('='*50)

# 아래와 같은 형태로 리스트를 만들어라
# ['*', '**', '***'...., '**********']

# 첫번째 방식
resultlist = []
for i in range(1,11):
    resultlist.append('*'*i)
print(resultlist)

# 두번째 방식
resultlist2 = []
resultlist2 = ['*'*i for i in range(1,11)]

print(resultlist2)

print('='*50)

# 리스트 다중 for
# 리스트안에 이중 for문이 있는 형태
# 리스트변수 = [결과값 for 명령문1 for 명령문2]

# ['col-1-1', 'col-1-2',....'col-3-3']

# 첫번째 방식
resultlist1 = []
for i in range(1,4):
    for j in range(1,6):
        resultlist1.append('col-'+ str(i)+'-'+str(j))
print(resultlist1)

# 두번쨰 방식 - 리스트 forfor
resultlist2 = []

resultlist2 = ['col-'+str(i)+'-'+str(j) for i in range(1,4) for j in range(1,6)]

print(resultlist2)

print('='*50)

# 퀴즈1
# 3단의 결과값에서 -1 한 값으로 리스트를 만들어라
# [2, 5, 8, ...]
list_1 = []
list_1 = [i*j-1 for i in range(3,4) for j in range(1,10)] # 한줄식
print(list_1)
# for i in range(3,4): 다중 for 문
#     for j in range(1,10):
#         list_1.append(i*j-1)
# print(list_1)



# 퀴즈1
# 구구단의 결과값으로 리스트를 만들어라
# [2, 4, ...., 63, 72, 81]

list_2 = []
list_2 = [i*j for i in range(2,10) for j in range(1,10)] # 한줄 식
print(list_2)
# for i in range(2,10): 다중 for 문
#     for j in range(1,10):
#         list_2.append(i*j)
# print(list_2)

print('='*50)

# 리스트 for + if
# 리스트안에 for문 + if 문이 있는 형태
# 리스트변수 = [결과값 for 명령문1 if 명령문2]
# 1~100까지의 숫자중에서 3의 배수만 리스트로 생성하여라
list_3 = []

for i in range(1,101):
    if i % 3 == 0:
        list_3.append(i)
print(list_3)

list_3 = [i for i in range(1,101) if i % 3 == 0]
print(list_3)


print('='*50)

# 1~15 사이의 숫자중에서 4의 배수는 제외하고 리스트로 생성하여라
resultlist1 = []
for i in range(1,16): # for + if 다중식
    if i%4 != 0:
        resultlist1.append(i)
print(resultlist1)

resultlist2 = []
resultlist2 = [i for i in range(1,16) if i%4 != 0] # 한줄식
print(resultlist2)





























