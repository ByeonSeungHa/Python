# 캐스팅
# 집합 => 리스트 list()
# 집합 => 튜플 tuple()
# 집합 => 딕셔너리 dict(enumerate())
# 집합 => 문자열 str() , '구분자'.join()




# 집합 합치기 = 합집합
# 집합변수3 = 집합변수1|집합변수2
# 집합변수3 = 집합변수1.union(집합변수2)

# 차집합
# 집합변수3 = 집합변수1-집합변수2
# 집합변수3 = 집합변수1.difference(집합변수2)


# 교집합
# 집합변수3 = 집합변수1&집합변수2
# 집합변수3 = 집합변수1.intersection(집합변수2)

# 대칭차집합 = 합집합-교집합
# 집합변수3 = 집합변수1^집합변수2
# 집합변수3 = 집합변수1.symmetric_difference(집합변수2)



# print(f' 합집합 = {setA|setB} {setA.union(setB)}') => |는 shift + \이다.
# {'토끼', '호랑이', '여우', '펭귄', '돼지', '사자'} {'토끼', '호랑이', '여우', '펭귄', '돼지', '사자'}
# print(f' 차집합 = {setA-setB} {setA.difference(setB)}')
# {'호랑이'} {'호랑이'}
# print(f' 교집합 = {setA&setB} {setA.intersection(setB)}')
# {'토끼', '돼지'} {'토끼', '돼지'}
# print(f' 대칭차집합 = {setA^setB} {setA.symmetric_difference(setB)}')
# {'펭귄', '여우', '호랑이', '사자'} {'펭귄', '여우', '호랑이', '사자'}