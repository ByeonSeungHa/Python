# 클래스
# 속성 + 메서드(동작)


# 클래스 생성 문법
# 클래스이름은 첫글자는 대문자로 지정
# class 클래스이름:
#   명령문

# 삼각형 클래스 선언
# 속성 => 가로, 높이, 색상
# 메서드 => 속성출력하기, 넓이구하기

# 생성자함수 문법
# class 클래스명:
#   def __init__(self, 인자):
#       self.인자 = 인자값
#       self.인자 = (인자값1, 인자값2,...) # 튜플형태

class Triangle:
    # 속성 정의 함수 = 생성자 함수
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    # 속성 출력 함수 정의 = 메서드
    def printInfo(self):
        print('='*50)
        print(f' 가로길이 : {self.width}')
        print(f' 세로길이: {self.height}')
        print(f' 색상 : {self.color}')

    # 삼각형 넓이를 구하는 함수 정의
    def printAread(self):
        print('=' * 50)
        print(f' 삼각형의 넓이는? : {(self.width*self.height)/2} ')


# 인스턴스 생성하기
# 클래스에서 생성하는 객체
# 인스턴스명은 첫글자는 소문자로 지정
# 인스턴스변수 = 클래스이름()
# 속성값을 전달해서 인스턴스 생성

# 첫번째 삼각형 생성
ti = Triangle(10, 20, 'red')
# 메서드 호출
# 인스턴스명.메서드명(인자)
ti.printInfo()
ti.printAread()
# print(ti) # <__main__.Triangle object at 0x00000284DC2623E0>

# 두번째 삼각형 생성
t2 = Triangle(50, 50, 'blue')
t2.printInfo()
t2.printAread()


# 타원 클래스 정의
class Circle:
    # 생성자(Constructor) => 원이름, 원색상, 반지름
    def __init__(self, cName, color, radius):
        self.cName = cName
        self.color = color
        self.radius = radius

    # 원의 속성을 출력하는 메서드 정의
    def info(self):
        print('='*50)
        print(f'원의 이름 : {self.cName}')
        print(f'원의 색상 : {self.color}')
        print(f'원의 반지름 : {self.radius}')

    # 원의 면적을 구하는 메서드 정의
    def area(self):
        print(f'{self.cName}원의 면적은? {3.14*self.radius**2}')


# 타원 클래스를 이용해서 인스턴스 생성
c1 = Circle('타원1', '노랑', 5)
c2 = Circle('타원2', '빨강', 10)

c1.info()
c2.info()
print('='*50)
c1.area()
c2.area()
























