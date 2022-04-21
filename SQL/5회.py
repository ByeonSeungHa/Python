# 다음
# 중
# 아래와
# 같은
# 2
# 건의
# 데이터
# 상황에서
# SQL의
# 수행
# 결과로
# 가장
# 적절한
# 것은? (단, 이해를
#      돕기 위해 ↓는 줄바꿈을 의미 →실제 저장값이 아님, CHR(10): ASCll
# 값 → 줄바꿈을
# 의미)  # 41
#
# 1.
# 2
# 2.
# 3
# 3.
# 5
# 4.
# 6
#
# 답
# 4
#
# 오라클환경에서
# 날짜형
# 데이터를
# 다룰
# 경우, 아래
# SQL
# 결과로
# 가장
# 적절한
# 것은?  # 42
#
# 아래
# SELECT
# TO
# CHAR(TO_DATE('2015.01.10 10', 'YYYY.MM.DD HH24')
#      + 1 / 24 / (60 / 10), 'YYYY.MM.DD HH24:MI:SS')
# FROM
# DUAL;
#
# 1.
# 2015.01
# .10
# 11: 01:00
# 2.
# 2015.01
# .10
# 10: 05:00
# 3.
# 2015.01
# .10
# 10: 10:00
# 4.
# 2015.01
# .10
# 10: 30:00
#
# 답
# 3
#
# 아래는
# SEARCHED_CASE_EXPRESSION
# SQL문장이다.이때
# 사용된
# SEARCHED_CASE_EXPRESSION은
# SIMPLE_CASE_EXPRESSION을
# 이용해
# 똑같은
# 기능을
# 표현할
# 수
# 있다.아래
# SQL
# 문장의
# ㄱ안에
# 들어
# 갈
# 표현을
# 작성하시오.(스칼라
# 서브쿼리는
# 제외함)  # 43
#
# 아래
# [SEARCHED_CASE_EXPRESSION 문장 사례]
# SELECT
# LOC,
# CASE
# WHEN
# LOC = NEW
# YORK
# THEN
# 'EAST'
# ELSE
# 'ETC'
# END
# asAREA
# FROM
# DEPT;
#
# [SIMPLE_CASE_EXPRESSION 문장 사례]
# SELECT
# LOC,
# CASE
# ㄱ
# ELSE
# 'ETC'
# END as AREA
# FROM
# DEPT;
#
# 답
# 3
#
# 팀별
# 포지션별
# FW, MF, DF, GK
# 포지션의
# 인원수와
# 팀별
# 전체
# 인원수를
# 구하는
# SQL을
# 작성할
# 때
# 결
# 과가
# 다른
# 것은? (보기 1은 SQL Sever 환경이고, 보기 2, 3, 4는 ORACLE 환경이다.)  # 44
#
# 1.
# ISNULL(SUM(CASE
# WHEN
# POSITION = 'FW'
# THEN
# 1
# END), 0) FW,
# ISNULL(SUM(CASE
# WHEN
# POSITION = 'MF'
# THEN
# 1
# END), 0) MF,
# ISNULL(SUM(CASE
# WHEN
# POSITION = 'DF'
# THEN
# 1
# END), 0) DF,
# ISNULL(SUM(CASE
# WHEN
# POSITION = 'GK'
# THEN
# 1
# END), 0) GK,
# COUNT(*)
# SUM
# FROM
# PLAYER
# GROUP
# BY
# THAM
# ID;
#
# 2.
# NVL(SUM(CASE
# POSITION = 'FW'
# THEN
# 1
# END), 0) FW,
# NVL(SUM(CASE
# POSITION = 'MF'
# THEN
# 1
# END), 0) MF,
# NVL(SUM(CASE
# POSITION = 'DF'
# THEN
# 1
# END), 0) DF,
# NVL(SUM(CASE
# POSITION = 'GK'
# THEN
# 1
# END), 0) GK,
# COUNT(*)
# SUM
# FROM
# PLAYER
# GROUP
# BY
# THAM
# ID;
#
# 3.
# NVL(SUM(CASE
# WHEN
# POSITION = 'FW'
# THEN
# 1
# END), 0) FW,
# NVL(SUM(CASE
# WHEN
# POSITION = 'MF'
# THEN
# 1
# END), 0) MF,
# NVL(SUM(CASE
# WHEN
# POSITION = 'DF'
# THEN
# 1
# END), 0) DF,
# NVL(SUM(CASE
# WHEN
# POSITION = 'GK'
# THEN
# 1
# END), 0)
# COUNT(*)
# SUM
# FROM
# PLAYER
# GROUP
# BY
# THAM
# ID;
#
# 4.
# NVL(SUM(CASE
# POSITION
# WHEN = 'FW'
# THEN
# 1
# END), 0) FW,
# NVL(SUM(CASE
# POSITION
# WHEN = 'MF'
# THEN
# 1
# END), 0) MF,
# NVL(SUM(CASE
# POSITION
# WHEN = 'DF'
# THEN
# 1
# END), 0) DF,
# NVL(SUM(CASE
# POSITION
# WHEN = 'GK'
# THEN
# 1
# END), 0) GK,
# COUNT(*)
# SUM
# FROM
# PLAYER
# GROUP
# BY
# THAM
# ID;
#
# 답
# 1
#
# 다음
# 중아래
# TAB1을
# 보고
# 각
# SQL
# 실행
# 결과를
# 가장
# 올바르게
# 설명한
# 것을
# 고르시오.  # 45
#
# 아래
# [TAB1]
# COL1
# COL2
# a
# NULL
# b
# ''
# c
# 3
# d
# 4
# e
# 3
#
# 1.
# SELECT
# COL2
# FRION
# TAB1
# WHERE
# COL1 = 'b'; -> 실행
# 결과가
# 없다.(공집합)
# 2.
# SELECT
# ISNULL(COL2, 'X')
# FROM
# TAB1
# WHERE
# COL1 = 'a'; -> 실행
# 결과로
# 'X'
# 를
# 반환한다.
# 3.
# SELECT
# COUNT(COL1)
# FROM
# TAB1
# WHERE
# COL2 = NULL; -> 실행
# 결과는
# 1
# 이다.
# 4.
# SELECT
# COUNT(COL2)
# FROM
# TAB1
# WHERE
# COL1
# IN('b', 'c'); ->실행
# 결과는
# 1
# 이다.
#
# 답
# 3
#
# 사원
# 테이블에서
# MGR의
# 값이
# 7698
# 과
# 같으면
# NULL을
# 표시하고, 같지
# 않으면
# MGR을
# 표시
# 하려고
# 한다.아래
# SQL
# 문장의
# ㄱ
# 안에
# 들어갈
# 함수명을
# 작성하시오  # 46
#
# 아래
# SELECT
# ENAME, EMPNO, MGR, ㄱ(MRG, 7698) as NM
# FROM
# EMP;
#
# 답
# 파티셔닝(Partitionning)
#
# 다음
# 중
# 아래
# 데이터를
# 가지고
# 있는
# EMP_Q
# 테이블에서
# 세개의
# SQL
# 결과로
# 가장
# 적절한
# 것은?  # 47
#
# 1.
# 0, NULL, NULL
# 2.
# 0, 에러
# 발생, 에러
# 발생
# 3.
# 에러
# 발생, 에러
# 발생, NULL
# 4.
# 0, 에러
# 발생, NULL
#
# 답
# 2
#
# 다음
# 중
# 아래와
# 같은
# 데이터
# 상황에서
# SQL의
# 수행
# 결과로
# 가장
# 적절한
# 것은?  # 48
#
# 1.
# 0
# 2.
# 1
# 3.
# 6
# 4.
# 14
#
# 답
# 4
#
# 아래의
# 각
# 함수에
# 대한
# 설명
# 중
# ㄱ, ㄴ, ㄷ
# 에
# 들어갈
# 함수를
# 차례대로
# 작성하시오.  # 49
#
# ㄱ(표현식1, 표현식2): 표현식1의
# 결과값이
# NULL이면
# 표현식2의
# 값을
# 출력한다.
# ㄴ(표현식1, 표현식2): 표현식1이
# 표현식2와
# 같으면
# NULL을, 같지
# 않으면
# 표현식1을
# 리턴한다.
# ㄷ(표현식1, 표현식2): 임의의
# 개수
# 표현식에서
# NULL이
# 아닌
# 최초의
# 표현식을
# 나타낸다.
#
# 답
# 4
#
# 다음
# 중
# 아래
# 각각
# 3
# 개의
# SQL
# 수행
# 결과로
# 가장
# 적절한
# 것은?  # 50
#
# 1.
# 20, 20, 20
# 2.
# 20, 10, 10
# 3.
# 10, 20, 20
# 4.
# 10, 10, 10
#
# 답
# 2
#
#
# 