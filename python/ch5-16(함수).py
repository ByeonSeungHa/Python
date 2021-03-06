# 모듈과 패키지
# 파이썬은 모듈(module)과 패키지(package) 형태로 라이브러리를 제공한다. 모듈은 다수의 함수나 클래스(class)를 묶어서
# 파일 형식(.py)으로 제공하며, 패키지는 비슷한 유형의 모듈이 많은 경우 폴더 형태로 묶어서 꾸러미로 제공한다.
# 따라서 라이브러리로 제공되는 함수나 클래스를 사용하기 위해서는 관련 모듈이나 패키지를 먼저 가져와야한다.
# 다음 [그림] 5-1은 파이썬 설치 과정에서 만들어진 파이썬 라이브러리이다.
# 라이브러리 > 패키지 > 모듈 이라고 생각하면 될거같다.

# 내장 함수
# 모듈이나 패키지에서 제공되는 함수를 이용하기 위해서는 먼저 import 명령어를 이용하여 파일에 포함시켜야한다.
# 예시)import random, import sys 등등(해당 모듈에서 제공하는 함수 또는 클래스를 가져온다.)
# 예시)from random import 함수명1, 함수명2....(해당 모듈에서 특정 함수만 가져온다.)

# import 방식 : 해당 패키지 또는 모듈이 포함하고 있는 모든 구성요소를 포함하는 방식이다.
#              명령문 형식은 간결하지만 구성요소가 많아지면 모든 구성요소가 메모리에 올라가기때문에 처리속도가 느려지고, 메모리 소모가 많다.
# from 방식 : 해당 패키지 또는 모듈이 포함하고 있는 구성요소 중에서 특정 요소만 포함시키는 방식이다.
#            명령문은 다소 복잡하지만 특정 요소만 메모리에 올라가기 때문에 속도가 빠르고, 메모리의 효율성이 높다.

# 사용자정의 함수
# 파이썬의 사용자정의 함수의 형식은 def 명령어 다음에 함수명을 지정하고, 인수를 받을 매개변수를 괄호안에넣는다
# 예시)def 함수명(인수 or 매개변수) 라고 생각하면되겠다. def hamsoo(n) or def hamsoo() 등등
# 실행문을 작성후 마지막에 return 명령문을 작성한다.


# 인수가 없는 함수
# def hamsoo():
# hamsoo() <-함수를 호출한다.

# 인수가 있는 함수
# def hamsoo(x,y):
# hamsoo(10,20) <- 함수를 호출한다. (z = x + y라고 한다면 z = 30이된다.

# return 있는 함수
# def hamsoo(x,y):
#     t=x+y (30)
#     s=x-y (-10)
#     m=x*y (200)
#     d=x/y (0.5)
#     return t, s, m, d
# x = int(input()), x = 10
# y = int(input()), y = 20


