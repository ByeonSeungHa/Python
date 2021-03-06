# (1) 지역변수 예
# 함수 바깥쪽에서 선언된 전역변수 x를 실인수로 함수를 호출할 경우 함수 내부에서 x에 50을 더해서 x는 100이 된다.
# 그리고 함수가 종료된 이후 x를 출력하면 100이 아닌 50이 출력된다.
# 결국 함수 내부에서 사용한 x는 함수 내부에서만 사용되는 지역변수이다.
# 지역변수는 해당 지역(함수 또는 블록)을 벗어나면 자동으로 소멸된다.


# (2) 전역변수 예
# global_func() 함수에서 'global x' 명령문은 함수 바깥쪽에서 선언된 전역변수 x를 사용한다는 의미이다.
# 따라서 함수 내부에서 x에 50을 더해진 값 100이 한수가 종료되어도 그대로 유지된다.
