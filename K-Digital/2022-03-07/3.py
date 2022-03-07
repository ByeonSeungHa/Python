# 자료선언
# 변수 < 콜렉션 (리스트, 튜플, 집합, 딕셔너리) <
# 함수 < 클래스 < 모듈(파일단위) < 패키지(폴더 단위)

# 모듈(Module)이란?
# 함수, 클래스의 집합 => 별도의 파일(*.py)로 생성

# 모듈의

# - 내부모듈
# : 파이썬에서 기본적으로 제공
# : datetime, time, math, random ....

# - 외부 모듈
# : pip/pip3(파이썬), conda(아나콘다)를 이용해서 별도 설치
# : 파이참에서는 [File]-[Settings]
#       [Project Interpreter]에서 확인
# : pandas, numpy, mathplotlib, seaborn, flask ...
# - 사용자정의 모듈
# : 필요에 의해서 직접 모듈로 등록한 후 사용



# 모듈 테스트1
# message.py (hello 함수 정의)
# 3.py (message.py에 정의된 hello, gugu 함수 호출)

# 1) message.py 파일 생성
#  hello() 함수 정의

# 2) 모듈 임포트 선언 1
# import 모듈이름
# message.py 플러그인
import message

# 3) 함수 호출
# 모듈이름.함수(인자)
# message.py 에 정의된 hello() 함수 호출
# message.hello()
# message.py 에 정의된 gugu(n) 함수 호출
# message.gugu(13)

# 모듈의 호출방법 2
# import 모듈이름 as 별칭(alias)
# 호출된 모듈의 함수 호출방법2
# 별칭.함수(인자)
# 3.py(message.py에 정의된 hello, gugu 함수 호출)
import message as m
# 2) 모듈안의 함수 호출
m.gugu(7)


# 모듈의 호출방법 3
# from 모듈이름 import 모듈함수
# 호출된 모듈의 함수 호출방법3
# 모듈함수(인자)

# 1) 모둘 함수 명으로 임포트
# message.py안의 hello, gugu 함수 사용 선언
from message import hello, gugu
# 2) 함수명으로만 호출
gugu(5)
hello()

# 패키지란?
# 폴더안의 모듈(파이썬 파일)
# 기본적으로 __init__.py 파일이 있어야한다.
# 파이참에서는 작업폴더 우측 버튼 클릭후 [New]-[Python Package] 명령 실행
# a 폴더안에 aa.py 안에 aaa() 함수 정의
# a 폴더(패키지) => aa.py(모듈) => aaa() 함수

# 임포트
# import 패키지명.모듈명
# import 패키지명.모듈명 as 별칭
# from 패키지명.모듈명 import 함수

# a 패키지안의 aa 모듈 임포트 선언
# import a.aa
from a.aa import aaa

# a 패키지안의 aa 모듈안에 선언된 aaa() 함수 호출
aaa()


















