# 어느 기업의 직원 테이블(EMP)이 직급(GRADE) 별로 사원 500명, 대리 100명, 과장 30명, 차장 10명,
# 부장 5명, 직급이 정해지지 않은(NULL) 사람 25명으로 구성되어 있을때, 다음 중 SQL문을 SQL1)부터
# SQL3)까지 순차적으로 실행한 결과 건수를 순서대로 나열한 것으로 가장 적절한 것은? # 51
#
# 아래
# SQL1) SELECT COUNT(GRADE) FROM EMP;
# SQL2) SELECT GRADE FROM EMP SHERE GRADE IN ('차장', '부장', 'NULL');
# SQL3) SELECT GRADE, COUNT(*) FROM EMP GROUP BY GRADE;
#
# 1. 670, 15, 5
# 2. 645, 40, 5
# 3. 645, 14, 6
# 4. 670, 40, 6
#
# 답 3
#
# 아래는 어느 회사의 광고에 대한 데이터 모델이다. 다음 중 광고매체 ID 별 최초로 게시한 광고명과
# 광고시작일자를 출력하기 위하여 아래 ㄱ에 들어갈 SQL로 옳은 것은? # 52
#
# SELECT C.광고매체명, B.광고명, A.광고시작일자
# FROM 광고게시 A, 광고 B, 광고매체 C, (ㄱ) D
# WHERE A.광고시작일자 = D.광고시작일자
# AND A.광고매체ID = D.광고매체ID
# AND A.광고ID = D.광고매체ID
# AND A.광고매체ID = C.광고매체ID
# ORDER BY C.광고매체명;
#
#
# 1. SELECT D.광고매체ID, MIN(D.광고시작일자) AS 광고시작일자
#    FROM 광고게시 D
#    WHERE D.광고매체ID = C.광고매체ID
#    GROUP BY D.광고매체ID
# 2. SELECT 광고매체ID, MIN(광고시작일자) AS 광고시작일자
#    FROM 광고게시
#    GROUP BY 광고매체ID
# 3. SELECT MIN(광고매체ID) AS 광고매체ID, MIN(광고시작일자) AS 광고시작일자
#    FROM 광고게시
#    GROUP BY 광고ID
# 4. SELECT MIN(광고매체ID) AS 광고매체ID, MIN(광고시작일자) AS 광고시작일자
#    FROM 광고게시
#
#
# 답 2
#
# 다음 중 오류가 발생하는 SQL 문장인 것은? # 53
#
# 1.
# SELECT 회원ID, SUM(주문금액) AS 합계
# FROM 주문
# GROUP BY 회원ID
# HAVING COUNT(*) > 1;
# 2.
# SELECT SUM(주문금액) AS 합계
# FROM 주문
# HAVING AVG(주문금액) > 100;
# 3.
# SELECT 메뉴ID, 사용유형코드, COUNT(*) AS CNT
# FROM 시스템사용이력
# WHERE 사용일시 BETWEEN SYSDATE - 1 AND SYSDATE
# GROUP BY 메뉴ID, 사용유형코드
# HAVING 메뉴ID = 3 AND 사용유형코드 = 100;
# 4.
# SELECT 메뉴ID, 사용유형코드, AVG(COUNT(*)) AS AVGCNT
# FROM 시스템사용이력
# GROUP BY 메뉴ID, 사용유형코드;
#
#
# 답 4
#
# 다음 중 아래와 같은 테이블 A에 대해서 SQL을 수행하였을 때의 결과로 가장 적절한 것은? # 54
#
# 1.
# 가: 009 나: A003 다: 600
# 가: 005 나: A002 다: 500
# 2.
# 가: 009 나: A003 다: 600
# 가: 005 나: A002 다: 500
# 가: 002 나: A001 다: 300
# 3.
# 가: 009 나: A003 다: 600
# 가: 005 나: A002 다: 500
# 가: 002 나: A001 다: 300
# 가: 010 나: A004 다: 200
# 4. 위의 SQL은 SELECT 절에 COUNT를 사용하지 않았으므로, HAVING절에서 오류가 발생한다.
#
# 답 2
#
# 다음 중 아래 SQL의 실행 결과로 가장 적절한 것은? # 55
#
# 1.
# ID
# 100
# 999
# 2.
# ID
# 999
# 100
# 3.
# ID
# 100
# 200
# 999
# 4.
# ID
# 999
# 200
# 100
#
# 답 2
#
# 다음 SQL 중 오류가 발생하는 것은? # 56
#
# 1.
# SELECT 지역 SUM(매출금액) AS 매출금액
# FROM 지역별매출
# GROUP BY 지역
# ORDER BY 매출금액 DESC;
# 2.
# SELECT 지역, 매출금액
# FROM 지역별매출
# ORDER BY 년 ASC;
# 3.
# SELECT 지역, SUM(매출금액) AS 매출금액
# FROM 지역별매출
# GROUP BY 지역
# ORDER BY 년 DESC;
# 4.
# SELECT 지역, SUM(매출금액) AS 매출금액
# FROM 지역별매출
# GROUP BY 지역
# HAVING SUM(매출금액) > 1000
# ORDER BY COUNT(*) ASC;
#
# 답 3
#
# 다음 중 ORDER BY 절에 대한 설명으로 가장 부적절한 것은? # 57
#
# 1. SQL 문장으로 조회된 데이터들을 다양한 목적에 맞게 특정 칼럼을 기준으로 정렬하는데 사용한다.
# 2. DBMS마다 NULL 값에 대한 정렬 순서가 다를 수 있으므로 주의하여야 한다.
# 3. ORDER BY 절에서 컬럼명 대신 Alias 명이나 컬럼 순서를 나타내는 정수도 사용이 가능하나, 이들을
# 혼용하여 사용할 수 없다.
# 4. GROUP BY 절을 사용하는 경우 ORDER BY 절에 집계 함수를 사용할 수도 있다.
#
# 답 3
#
#
# 다음 SQL의 실행 결과로 가장 적절한 것은? # 58
#
# 1.
# ID: B AMT: 300
# ID: A AMT: 200
# ID: C AMT: 100
# ID: A AMT: 50
# 2.
# ID: A AMT: 200
# ID: A AMT: 50
# ID: B AMT: 300
# ID: C AMT: 100
# 3.
# ID: A AMT: 50
# ID: C AMT: 100
# ID: A AMT: 200
# ID: B AMT: 300
# 4.
# ID: B AMT: 300
# ID: A AMT: 200
# ID: A AMT: 50
# ID: C AMT: 100
#
# 답 2
#
# 다음 중 SELECT 문장의 실행 순서를 올바르게 나열한 것은? # 59
#
# 1. SELECT - FROM - WHERE - GROUP BY - HAVING - ORDER BY
# 2. FROM - SELECT - WHERE - GROUP BY - HAVING - ORDER BY
# 3. FROM - WHERE - GROUP BY - HAVING - ORDER BY - SELECT
# 4. FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY
#
# 답 4
#
# 아래의 팀별성적 테이블에서 승리건수가 높은 순으로 3위까지 출력하되 3위의 승리건수가 동일한
# 팀이 있다면 함께 출력하기 위한 SQL 문장으로 올바른 것은? # 60
#
# 1.
# SELECT TOP(3) 팀명, 승리건수
# FROM 팀별성적
# ORDER BY 승리건수 DESC;
# 2.
# SELECT TOP(3) 팀명, 승리건수
# FROM 팀별성적;
# 3.
# SELECT 팀명, 승리건수
# FROM 팀별성적
# WHERE ROWNUM <= 3
# ORDER BY 승리건수 DESC;
# 4.
# SELECT TOP(3) WITH TIES 팀명, 승리건수
# FROM 팀별성적
# ORDER BY 승리건수 DESC;
#
# 답 4
