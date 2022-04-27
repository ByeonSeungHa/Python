# SET OPERATOR 중에서 수학의 교집합과 같은 기능을 하는 연산자로 가장 적절한 곳운> # 81
#
# 1. UNION
# 2. INTERSECT
# 3. MINUS
# 4. EXCEPT
#
# 답 2
#
# 다음 중 아래의 EMP 테이블의 데이터를 참조하여 실행한 SQL의 결과로 가장 적절한 것은? # 82
#
# 아래
# SELECT ENAME AAA, JOB AAB
# FROM EMP
# WHERE EMPNO = 7369
# UNION ALL
# SELECT ENAME BBA, JOB BBB
# FROM EMP
# WHERE EMPNO = 7566
# ORDER BY 1, 2;
#
# 1.
# AAA	AAB
# SMITH	CLERK
# JONES	MANAGER
# 2.
# AAA	AAB
# JONES	MANAGER
# SMITH	CLERK
# 3.
# BBA	BBB
# SMITH	CLERK
# JONES	MANAGER
# 4.
# BBA	BBB
# JONES	MANAGER
# SMITH	CLERK
#
# 답 2
#
# 다음 중 아래 TBL1, TBL2 테이블에 대해 SQL을 수행한 결과인 것은? # 83
#
# 아래
# [테이블 : TBL1]
# COL1	COL2
# AA	A1
# AB	A2
# [테이블 : TBL2]
# COL1	COL2
# AA	A1
# AB	A2
# AC	A3
# AD	A4
#
# [SQL]
# SELECT COL1, COL2, COUNT(*) AS CNT
# FROM (SELECT COL1, COL2
# 	FROM TBL1
# 	UNION ALL
# 	SELECT COL1, COL2
# 	FROM TBL2
# 	UNION
# 	SELECT COL1, COL2
# 	FROM TBL1)
# GROUP BY COL1, COL2;
#
# 1.
# COL1	COL2	CNT
# AA	A1	1
# AB	A2	1
# AC	A3	1
# AD	A4	1
# 2.
# COL1	COL2	CNT
# AA	A1	2
# AB	A2	2
# AC	A3	1
# AD	A4	1
# 3.
# COL1	COL2	CNT
# AA	A1	3
# AB	A2	3
# AC	A3	1
# AD	A4	1
# 4.
# COL1	COL2	CNT
# AA	A1	3
# AB	A2	3
# AC	A3	2
# AD	A4	2
#
# 답 1
#
# 다음 중 아래에서 테이블 T1, T2에 대한 가, 나 두개의 쿼리 결과 조회되는 행의 수로 가장 적절한
# 것은? # 84
#
# 아래
# T1(A,B,C)
# A	B	C
# A3	B2	C3
# A1	B1	C1
# A2	B1	C2
# T2(A,B,C)
# A	B	C
# A1	B1	C1
# A3	B2	C3
#
# 가. SELECT A, B, C FROM R1
# 	UNION ALL
# 	SELECT A, B, C FROM R2
#
# 나. SELECT A, B, C FROM R1
# 	UNION
# 	SELECT A, B, C FROM R2
#
# 1. 가: 5개, 나 : 3개
# 2. 가: 5개, 나 : 5개
# 3. 가: 3개, 나 : 3개
# 4. 가: 3개, 나 : 5개
#
# 답 1
#
# 다음 중 아래와 같은 집합이 존재 할 때, 집합 A와 B에 대하여 집합연산을 수행한 결과 집합 C가 되는
# 경우 이용되는 데이터베이스 집합연산은? # 85
#
# 아래
# 집합 A = {가, 나, 다, 라},
# 집합 B = {다, 라, 마, 바},
# 집합 C = {다, 라}
#
# 1. Union
# 2. Difference
# 3. Intersection
# 4. Product
#
# 답 3
#
# 아래와 같은 데이터 모뎅레 대한 설명으로 가장 적절한 것은? # 86
# (단, 시스템적으로 회원기본정보와 회원상세정보는 1:1, 양쪽 필수 관계임을 보장한다.)
#
# 1. 회원ID 컬럼을 대상으로 (회원기본정보 EXCEPT 회원상세정보) 연산을 수행하면 회원상세정보가
# 등록되지 않는 회원ID가 추출된다.
# 2. 회원ID 컬럼을 대상으로 (회원기본정보 UNION ALL 회원상세정보) 연산을 수행한 결과의 건수는
# 회원기본정본의 전체건수와 동일하다.
# 3. 회원ID 컬럼을 대상으로 (회원기본정보 INTERSECT 회원상세정보) 연산을 수행한 결과의 건수와
# 두 테이블을 회원ID로 JOIN 연산을 수행한 결과의 건수는 동일하다.
# 4. 회원ID 컬럼을 대상으로 (회원기본정보 INTERSECT 회원상세정보) 연산을 수행한 결과와 (회원기본
# 정보 UNION 회원상세정보) 연산을 수행한 결과는 다르다.
#
# 답 3
#
# 아래와 같은 데이터 상황에서 아래의 SQL을 수행할 경우 정렬 순서상 2번째 표시될 값을 적으시오.
# # 87
#
# 아래
# TAB1
# C1	C2	C3
# 1		A
# 2	1	B
# 3	1	C
# 4	2	D
#
# 답 C
#
# 다음 중 Oracle 계층형 질의에 대한 설명으로 가장 부적절한 것은? # 88
#
# 1. START WITH절은 계층 구조의 시작점을 지정하는 구문이다.
# 2. ORDER SIBILINGS BY절은 형제 노드 사이에서 정렬을 지정하는 구문이다.
# 3. 순방향전개란 부모 노드로부터 자식 노드 방향으로 전개하는 것을 말한다.
# 4. 루트 노드의 LEVEL 값은 0이다.
#
# 답 4
#
# 다음 중 아래와 같은 사원 테이블에 대해서 SQL을 수행하였을 때의 결과로 가장 적절한 것은? # 89
#
# 아래
# [테이블 : 사원]
# 사원번호(PK)	사원명	입사일자		매니저사원번호(FK)
# 001		홍길동	2012-01-01	NULL
# 002		강감찬	2012-01-01	001
# 003		이순신	2013-01-01	001
# 004		이민정	2013-01-01	001
# 005		이병헌	2013-01-01	NULL
# 006		안성기	2014-01-01	005
# 007		이수근	2014-01-01	005
# 008		김병만	2014-01-01	005
#
# [SQL]
# SELECT 사원번호, 사원명, 입사일자, 매니저사원번호
# FROM 사원
# START WITH 매니저사원번호 IS NULL
# CONNECT BY, PRIOR 사원번호 = 매니저사원번호
# AND 입사일자 BETWEEN '2013-01-01' AND '2013-12-31'
# ORDER SIBLINGS BY 사원번호;
#
# 1.
# 사원번호(PK)	사원명	입사일자		매니저사원번호(FK)
# 001		홍길동	2012-01-01	NULL
# 003		이순신	2013-01-01	001
# 004		이민정	2013-01-01	001
# 005		이병헌	2013-01-01	NULL
# 2.
# 사원번호(PK)	사원명	입사일자		매니저사원번호(FK)
# 003		이순신	2013-01-01	001
# 004		이민정	2013-01-01	001
# 005		이병헌	2013-01-01	NULL
# 3.
# 사원번호(PK)	사원명	입사일자		매니저사원번호(FK)
# 001		홍길동	2012-01-01	NULL
# 4.
# 사원번호(PK)	사원명	입사일자		매니저사원번호(FK)
# 001		홍길동	2012-01-01	NULL
# 005		이병헌	2013-01-01	NULL
# 006		안성기	2014-01-01	005
# 007		이수근	2014-01-01	005
# 008		김병만	2014-01-01	005
#
# 답 1
#
# 다음 중 계층형 질의문에 대한 설명으로 가장 부적절한 것은? # 90
#
# 1. SQL Sever에서의 계층형 질의문은 CTE(Common Table Expression)를 재귀 호출함으로써 계층
# 구조를 전개한다.
# 2. SQL Sever에서의 계층형 질의문은 앵커 멤버를 실행하여 기본결과 집합을 만들고 이후 재귀 멤버를
# 지속적으로 실행한다.
# 3. 오라클의 계층형 질의문에서 WHERE 절은 모든 전개를 진행한 이후 필터 조건으로서 조건을 만족
# 하는 데이터만을 추출하는데 활용된다.
# 4. 오라클의 게층형 질의문에서 'PRIOR 자식 = 부모'형태로 사용하면 순방향 전개로 수행 된다.
#
# 답 4
# 
