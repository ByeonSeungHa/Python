n = int(input()) # 정수로 받아온다

for _ in range(n):
    cnt, word = input().split() # 숫자와 문자를 변수로 지정하고 각각 받아온다.
    for x in word:
        print(x*int(cnt), end='')
        # *(곱셈)연산자를 이용해서 변수 x를  입력받은 cnt만큼 반복한다.
        # 출력 형태는 숫자가 아닌 문자열을 옆으로 붙여 출력해야 하기 때문에 end에 ''만 붙여서 공백없이 출력되게 한다.
        # end='' 옆으로 붙임
    print()  # end를 이용하지 않을때는 줄 넘김이 기본값이지만 출력할 값이 여러개면 공백으로 출력 값이 구분된다.