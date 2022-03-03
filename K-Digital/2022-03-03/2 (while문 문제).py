# 반복문 : while
# while 조건:
#      실행명령
# 조건이 True 이면 명령을 실행해라

# hello world 를 n번 출력 하여라

n = 1 # 초기치

while n <= 10:
    print(f' {n} : Hello world')
    n += 1 # 증감
print('while 테스트 종료')

# 88~1 까지 가로로 출력하기

n = 88 # 초기치

while n > 0:
    print(n, end=' ')
    n -= 1 # 증감
print('\n\n while 테스트 종료')



# 퀴즈2 = 1~100까지의 합 출력하기
# 1+2+....+100=?
# 1~100까지의 합은?

print('='*50)

n=1
total = 0
while n <= 100:
    total += n
    # print(n,end=' ')
    n+= 1 # 증감
print(f'1~100Rkwldml gkqdms? {total}')
print('\n\n while 테스트 종료')


# while 문 + if 문
# 1~100 사이의 숫자중에서 5의 배수이거나 7의 배수이면 출력
n = 1
while n <= 100: # 1 ~100 사이라고 나타내는 식
    if n % 5 == 0 or n % 7 == 0:
        print(n, end=' ')
    n += 1
print('\n\n while 테스트 종료')
# 1~50 사이의 숫자중에서 3의 배수이거나 8의 배수로 구성된 리스트를 생성하여라

print('='*50)

a = 1
num_list = []
while a <= 50:
    if a % 3 ==0 or a % 8 ==0:
        num_list.append(a)
    a += 1
print(f' num_list = {num_list} 총갯수는? { len(num_list)}')
print('\n\n while 테스트 종료')


# 퀴즈
# 1~20까지 숫자를 출력하여라. 한줄에 5개씩 출력하여라
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# ...
# n = 0
# count = 0
# while n <20:
#     n+=1
#     count+=1
#     print(n, end=' ')
#     if count%5==0:
#         print() # 개행
#

n = 1
while n<=20:
    if (n%5==0):
        print(n)
    else:
        print(n, end = ' ')
    n += 1


# 다중 while 문
# while 조건1:
#   while 조건2:
#       명령문2
#   명령문1

# 점선 출력후 문단 3번찍기 n번 반복하기

n1 = 1
# n2 = 1
while n1 <= 3:
    print('-'*30)
    n2 = 1
    while n2 <= 3:
        print(n2)
        n2 +=1
    n1+=1

# 퀴즈
# 2~9단 출력하기

# n단 출력
n = 2
cnt = 1
print(f'{n} 단출력')
while cnt<=9:
    print(f' {n} X {cnt} = {n*cnt}')
    cnt+=1

# 2~9단 출력

n = 2
while n<=9:
    print(f'\n{n} 단 출력')
    cnt = 1
    while cnt<=9:
        print(f' {n} X {cnt} = {n*cnt}')
        cnt+=1
    n+=1

# while 문을 이용한
# 리스트,딕셔너리,문단, 튜플 아이템 출력

# while 문 이용해서 리스트 요소 출력하기
# 인덱싱위치 번째 요소는 인덱싱위치의값
# list1 = ['사과', '바나나', '수박', '포도']

'''
0 번째 요소는  사과
1 번째 요소는  바나나
2 번째 요소는  수박
3 번째 요소는  포도
'''

print('='*50)

fruitlist = ['사과', '바나나', '수박', '포도']
# print(fruitlist[0])


i = 0
while i<len(fruitlist) :
    print(f' {i}번째 요소는 {fruitlist[i]}')
    i += 1

# 문자열을 세로로 출력하여라
print('='*50)
txt = 'abcdefg'

i = 0
while i<len(txt):
#   print((' '*i) + txt[i]) # 사선으로 출력
#   print(txt[i]) # 세로으로 출력
#   print(('='*(i*2)) + txt[i]) # 2칸너비로 사선으로 출력
    i += 1



# 퀴즈
# 아래와 같이 문자열을 출력하여라
# txt = 'abcde'
'''
                a
            b
        c
    d
e
'''

# print('='*50)
# txt = 'abcde'
# i = 0 # 인덱스
# count = len(txt) # 공백
#
# while i < len(txt):
#     print((' '*count)+txt[i])
#     i+=1
#     count -= 1

txt = 'abcde'
i = 0
while i < len(txt):
#    print(len(txt)-1-i,i)
    print(('   '*(len(txt)-1-i)) + txt[i])
    i += 1


# break
# 반복문 안에서 사용
# 명령문 실행시 제어문에서 탈출한다.
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.
# 무한루프의 종료 조건시 사용

print('='*50)

n=1
while n <= 5:
    print(n)
    if (n==3):
        break
    n += 1
print(' break 테스트 종료')



# 무한루프 + if + break
# while True조건:
#   if 블록을 빠져나갈 조건:
#      break

# 입력값이 x 또는 X이면 종료
# while True:
#     ans = input('입력 =>')
#     # 무한루프에서 탈출 조건
#     if ans == 'x' or ans == 'X':
#         break
# print(' break 테스트 종료')

# 대소문자 상관없이 yes 입력시 종료
# yes, YES, Yes, yEs, YEs
# 입력값을 모두 대문자 변경 upper()
# 입력값을 모두 소문자 변경 lower()

print('='*50)

word = 'yes'
print(word, word.upper(), word.lower()) # Yes YES yes


print('='*50)
# while True:
#     ans = input('입력 =>')
#     # 입력값을 대문자로 변경해서 YES 인지 판독
#     if ans.upper() == 'YES':
#         break
# print(' break 테스트 종료')


# continue
# 제어문 안에서 사용
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.

# 1~10 사이 숫자중에서 5를 제외하고 출력하여라


n = 0
while n<=9:
    n += 1
    if n == 5:
        continue # continue는 지정된 숫자를 무시한다. 지금 지정된 수는 5이다.
    print(n, end=' ')
print(' continue 테스트 종료 ') # 1 2 3 4 6 7 8 9 10  continue 테스트 종료









