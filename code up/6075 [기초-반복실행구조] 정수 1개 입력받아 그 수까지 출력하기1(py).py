# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

a = int(input())
b = int(0)
while b<=a:
    print(int(b), end=' ')
    b += 1

