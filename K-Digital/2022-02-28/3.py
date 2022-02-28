# 문자열 연산자
# + => 연결
# *숫자=>반복


firstName = '선우'
secondName = '영선'
print(firstName, secondName, firstName+secondName)
print('='*5, 'python='*3)

# 문자열 인덱싱
# 인덱싱이란?  문자열의 위치를 숫자로 표시
# 인덱싱의 첫 위치는 0
# 인덱싱의 마지막 위치는 -1
# 문자열변수[인덱스값]

# 문자열 전체길이는?
# len(문자열이나 문자열변수)?

txt = 'abcdefg'
print(txt[0]) # a
print(txt[-1]) # g
print(txt[5]) # g
print(txt[-5]) # b
print(len(txt)) # 7

# 퀴즈
# 아래 변수에서 마지막 시를 출력하는 3가지 방법
txt2 = '도레미파솔라시'

print(txt2[6])
print(txt2[-1])
print(txt2[len(txt2)-1])
print(txt2[6:7]) # 슬라이싱을 사용한 방법이다.



# 문자열 슬라이싱이란?
# 문자열의 일부를 잘라서 표시
# 문자열변수[start:end:step]
# 문자열변수[start:end]
# 문자열변수[start:]
# 문자열변수[:end]
# 문자열변수[::step]
# start 부터 end-1 까지 step 수만큼 건너뛰기

txt3 = '가나다라마바사아'
print('-'*50)
print(txt3[:]) # 가나다라마바사아
print(txt3[0:4]) # 가나다라
print(txt3[1:3]) # 나다
print(txt3[:3]) # 가나다
print(txt3[5:]) # 바사아
print(txt3[-3:]) # 바사아
print(txt3[-5:-2]) # 라마바
print(txt3[::2]) # 가다마사 # 홀수 째 글자 출력
print(txt3[1::2]) # 나라바아 # 짝수 째 글자 출력
print(txt3[::-1]) # 아사바마라다나가 # 역순으로 출력
print(txt3[-2:-5]) # 출력 불가



# %를 이용한 포맷팅
# %자료형
# %d / %s / %전체자리수.소숫점자리이하숫자 f / %o / %x
# print(' 문자열 %자료형 ' % 변수)
# print(' 문자열 %자료형1 %자료형2 ' % (변수1, 변수2))


age = 19
userName = '홍길동'
mailing = True

# 학생 정보 나이=> 19, 이름=> 홍길동, 메일링=> True
print('학생 정보','나이=', age, '이름=>', userName, '메일링=', mailing)
print('학생 정보 나이= %d,이름=> %s 메일링= %s' % (age,userName,mailing))



# 10진수, 8진수, 16진수로 출력
print('10진수 %d , 8진수 %o , 16진수 %x' % (age,age,age))




# %전체자릿수.소수점이하자릿수f
# %.소수점이하자릿수f
pi = 3.14156748
print('pi = %f' % pi) # 3.141567
print('pi = %.4f' % pi) # 3.1416
print('pi = %20.4f' % pi) #                3.1416

# %로 공백 지정
# %양수숫자Style(s/f/d/x/o) : 왼쪽에 공백 생성
# %음수숫자Style9s/f/d/x/o) : 오른쪽에 공백 생성

userName = '홍길동'
userNumber = 123.45
print('user Name : %10s ** ' % userName) # 왼쪽에 공백이생김 #         홍길동 **
print('user Name : %-10s ** ' % userName) # 오른쪽에 공백이 생김 # 홍길동        **
print('userNumber : %10d ** ' % userNumber) # userNumbers #         123 **
print('userNumber : %-15f ** ' % userNumber) # userNumbers #  123.450000      **


# format 을 이용한 출력방식
# ' 문자열1 {} {} 문자열2'.format(변수1, 변수2)
# 소숫점 처리 => {위치인덱스:전체자릿수.소수점이하자릿수f}
userName = '홍길동'
userNumber = 123.45678
print('='*50)
print('user Name : {}  userNumber : {}'.format(userName, userNumber) )
# user Name : 홍길동  userNumber : 123.45678
print('user Name : {0}  userNumber : {1:.2f}'.format(userName, userNumber) )
# user Name : 홍길동  userNumber : 123.46
print('user Name : {0}  userNumber : {1:15.2f}'.format(userName, userNumber) )
# user Name : 홍길동  userNumber :          123.46

# f 문자열 포맷팅 : 3.6 이상 지원
# f' 문자열 {변수명이나 변수를이용한수식} '

# f 포맷팅 소수점 처리
# f' 문자열 {변수명:전체자릿수.소숫점이하자릿수f} '

# f' 문자열 공백, 대체문자여백 지정
# f' 문자열 {변수명:>숫자} : 왼쪽여백생성
# f' 문자열 {변수명:<숫자} : 오른쪽여백생성
# f' 문자열 {변수명:^숫자} : 좌우여백생성
# f' 문자열 {변수명:대체문자>숫자} : 왼쪽에 대체문자반복
# f' 문자열 {변수명:대체문자<숫자} : 오른쪽에 대체문자반복
# f' 문자열 {변수명:대체문자^숫자} : 좌우 대체문자 반복


userName = '홍길동'
userNumber = 123.45678

print('='*50)
print(f'user Name : {userName}  userNumber : {userNumber}')
# user Name : 홍길동  userNumber : 123.45678
print(f'user Name : {userName:>20}  userNumber : {userNumber:.2f}')
# user Name :                  홍길동  userNumber : 123.46
print(f'user Name : {userName:^20}  userNumber : {userNumber:15.2f}')
# user Name :         홍길동           userNumber :          123.46
print(f'user Name : {userName:$<20}  userNumber : {userNumber:.2f}')
# user Name : 홍길동$$$$$$$$$$$$$$$$$  userNumber : 123.46

# 퀴즈
# 아래와 같이 변수를 지정하고
# humidity = 82
# temperature = -1.85674
# % 포맷, format(), f' 포맷 3가지 방식을 이용하여 다음과 같이 출력하여라

'''
오늘의 날씨 : 맑음, 습도 82%, 현재기온 -1.8
'''

humidity = 82
temperature = -1.83674

print('오늘의 날씨 : 맑음, 습도 %d%%, 현재기온 %.1f'%(humidity, temperature))
print('오늘의 날씨 : 맑은, 습도 {}%, 현재기온 {:.1f}'.format(humidity,temperature))
print(f'오늘의 날씨 : 맑음, 습도 {humidity}%, 현재기온 {temperature:.1f}')


# 문자열 함수
# 문자열변수.함수명(옵션)
# 문자열.함수명(옵션)

# 샘플 문자열 만들기
# http://www.lipsum.com 이용 -> 샘플 문자 열을 가져올 수 있는 사이트

sample = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged.
'''


print('='*50)
print(sample)


# 특정 문자열의 갯수 출력
# 문자열변수.count(찾고자하는문자열)
print('is 글자의 갯수는?', sample.count('i'))

# 문자열 교체하기
# 문자열변수.replace(찾고자하는문자열, 교체문자열)
# i => I

print(sample.replace('i', 'I'))


