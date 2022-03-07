# 파일입출력함수

# 샘플 파일 준비
# data.zip 파일을 작업폴더(예:workspace20220228)안에 data 폴더에 압축해제
# 하위 폴더 data 확인
# data 폴더안에 자료 파일 목록 확인


# 현재 작업폴더 위치 확인하기
import os
print(os.getcwd()) # C:\Users\User\Desktop\workspace\K-Digital\2022-03-07

# 현재 작업폴더의 파일 목록과 폴더를 리스트로 표시
print(os.listdir(os.getcwd()))
# data 폴더안의 파일 목록
print(os.listdir(os.getcwd()+'\data'))

# 파일입출력 (텍스트파일 기준)
# CRUD


# 파일입출력
# 파일변수  = open(파일경로, 'r'/'w'/'a',
#                    encoding='utf-8/cp949')
# 파일변수.파일입출력함수(옵션)

# 파일읽기
# 파일변수 생성
# 파일변수  = open(파일경로, 'r',
#                     encoding='utf-8/cp949')
# 파일변수.read() : 파일전체 문자열 구조 =>  문자열
# 파일변수.readline() : 파일에서 첫줄만 읽기 => 문자열
# 파일변수.readlines() : 각행이 리스트 구조로 변경 => 리스트

# data/data_eng.txt => 숫자 리스트 변환후 총점과 평균을 출력하여라.
# 1) 파일변수 생성
f = open('data/data_eng.txt', 'r', encoding='utf-8')
# 2) 데이타 변수에 저장
engList = f.readlines() # 문자열 리스트
# 3) 숫자 리스트로 변경
engList2 = []
for i in engList:
    engList2.append(float(i))
# 4) 출력
print('='*50)
print(engList2) # 전체출력
print(f' 총점 : {sum(engList2)}  평균 : {sum(engList2)/len(engList2)}') # 전체출력
# 5) 파일닫기
f.close()


# 파일 쓰기
# 새로운 파일이 생성되면서 내용이 추가된다.
# 기존에 파일이 있다면 덮어쓰기된다.
# 파일변수 = open( 생성파일경로, 'w', encoding='cp949/utf-8')
# 파일변수.write(문자열)
# 파일변수.close()


# output 폴더 생성 후
# output/test1.txt 파일 생성

# output 폴더 생성 후
# output/test1.txt 파일 생성

# 1) 파일 변수 생성
f = open( 'output/test1.txt', 'w', encoding='utf-8')
# 2) 데이타를 파일에 쓰기
f.write('='*50)
f.write('\n\t애국가')
f.write('\n동해물과 백두산이')
f.write('\n마르고 닳도록')
f.write('\n하느님이 보우하사 우리나라 만세')

# 3) 파일 닫기
f.close()

# output/test2.txt 파일에 1~20까지의 숫자를 저장하여라
# 1) 파일 변수 생성
f = open('output/test2.txt', 'w', encoding='utf-8')
# 2) 데이터를 파일에 쓰기
for i in range(1,21):
    #  f.write(i) # TypeError: write() argument must be str, not int
    f.write(f'\n{i}')
# 3) 파일 닫기
f.close

# 퀴즈 구구단 전체를 # output/test3.txt 파일에 아래와 같은 스타일로 저장하여라.

'''
    2 단 
2 X 1 = 2
2 X 2 = 4

...

    9 단 
9 X 1 = 9
9 X 2 = 9

9 X 9 = 81 
'''


# 1) 파일 변수 생성
f = open( 'output/test3.txt', 'w', encoding='utf-8')
# 2) 데이타를 파일에 쓰기
for i in range(2,10):
    f.write(f'\n{i}단')
    for j in range(1,10):
        f.write(f'\n{i} x {j} = {i*j}')
    f.write('\n')
    f.write('='*20)

# 3) 파일 닫기
f.close()


# 내용추가하기
# 기존 파일에 내용이 추가된다.
# 파일변수 = open( 생성파일경로, 'a', encoding='cp949/utf-8')
# 파일변수.write(문자열)
# 파일변수.close()

# output/test4.txt 파일에 첫번째 리스트의 데이타를 저장하여라
foodList = ['라면', '김밥', '밀면']
# 1) 파일 변수 생성
f = open( 'output/test4.txt', 'w', encoding='utf-8')
# 2) 데이타를 파일에 쓰기
for i in  foodList:
    f.write('\n' + i)
# 3) 파일 닫기
f.close()
# 4) test4.txt 파일에서 결과 확인


# output/test4.txt 파일에 두번째 리스트의 데이타를 추가로 저장하여라
fruitList = ['오렌지', '사과', '포도']
# 1) 파일 변수 생성
f = open( 'output/test4.txt', 'a', encoding='utf-8')
# 2) 데이타를 파일에 쓰기
f.write('\n====================')
for i in  fruitList:
    f.write('\n' + i)
# 3) 파일 닫기
f.close()
# 4) test4.txt 파일에서 결과 확인


# with 문과 파일 입출력
# 파일.close() 를 사용할 필요가 없다.
# with open(파일경로, 'a'/'w'/'r', encoding='uft-8/cp949')
#  as 파일변수:
#   명령문



# with 문과 파일 입출력
# 파일.close() 를 사용할 필요가 없다.
# with open(파일경로, 'a'/'w'/'r', encoding='uft-8/cp949')
#  as 파일변수:
#   명령문




# with 문과 파일 입출력
# 파일.close() 를 사용할 필요가 없다.
# with open(파일경로, 'a'/'w'/'r', encoding='uft-8/cp949')
#  as 파일변수:
#   명령문

# with 문을 이용한 파일 읽기
with open('data/Yesterday.txt','r') as f:
    result = f.read()
    print(result[:10])
print('\n\n파일 읽기 테스트 완료 \n\n')

# with문을 이용한 파일쓰기
with open('data/test2.txt','w') as f:
    f.write('파일 쓰기 테스트 \n'*10)
print('\n\n파일 쓰기 테스트 완료 \n\n')

# with문을 이용한 내용 추가
with open('data/test2.txt','a') as f:
    f.write('내용 추가 테스트 \n'*3)


# with 문과 파일 입출력
# 파일.close() 를 사용할 필요가 없다.
# with open(파일경로, 'a'/'w'/'r', encoding='uft-8/cp949')
#  as 파일변수:
#   명령문

# with 문을 이용한 파일 읽기
# (1) 파일생성
with open('data/Yesterday.txt','r') as f:
    # (2)한줄만 저장
    data = f.readline()
    # (3)출력
    print(data)
print('='*50)


# with 문을 이용한 파일 쓰기
# 1) 파일 변수 생성
with open('output/test5.txt','w', encoding='utf-8') as f:
    # 2) 데이타를 파일에 쓰기
    for i in range(2,10):
        f.write(f'\n{i}단')
        for j in range(1,10):
            f.write(f'\n{i} x {j} = {i*j}')
        f.write('\n')
        f.write('='*20)


# 퀴즈
# data/black.txt 파일에
# data/white_before.txt파일의 내용을 추가하여
# output/color.txt 파일로 저장하여라
# 1) data/black.txt 읽기 => output/color.txt.저장
# 1) data/white_before.txt 읽기 => output/color.txt.저장


# 1) data/black.txt 읽기 => temp
with open('data/black.txt','r', encoding='utf-8') as f:
    temp = f.read()

# 2) temp => output/color.txt
with open('output/color.txt','w', encoding='utf-8') as f:
    f.write('\n\n'+temp)
    print('내용 추가가 완료되었습니다. ')

# 3) data/white_before.txt 읽기 => temp
with open('data/white_before.txt','r', encoding='utf-8') as f:
    temp = f.read()

# 4) temp => output/color.txt 추가
with open('output/color.txt','a', encoding='utf-8') as f:
    f.write('\n\n'+temp)
    print('내용 추가가 완료되었습니다. ')














