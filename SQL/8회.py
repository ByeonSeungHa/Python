# 아래의 사례1은 Cartesian Product를 만들기 위한 SQL 문장이며 사례1과 같은 결과를 얻기 위해
# 시례2 SQL 문장의 ㄱ안에 들어갈 내용을 작성하시오. # 71
#
# 아래
# [사례1]
# SELECT ENAME, DNAME
# FROM EMP, DEPT
# ORDER BY ENAME;
#
# [사례2]
# SELECT ENAME, DNAME
# FROM EMP ㄱ DEPT
# ORDER BY ENAME;
#
# 답 CROSS JOIN
#
# 다음 중 아래 테이블들을 대상으로 SQL 문장을 수행한 결과로 가장 적절한 것은? # 72
#
# 아래
# [SQL]
# SELECT A.고객번호, A.고객명, B.단말기ID, B.단말기명, C.OSID, C.OS명
# FROM 고객 A LEFT OUTER JOIN 단말기 B
# ON (A.고객번호 IN (11000, 12000) AND A.단말기ID = B.단말기ID) LEFT OUTER JOIN OS C
# ON (B.OSID = C.OSID)
# ORDER BY A.고객번호;
#
# 1.
# 2.
# 3.
# 4.
#
# 답 1
#
# 다음 중 아래 (1), (2), (3)의 SQL에서 실행결과가 같은 것은? # 73
#
# (1)
# SELECT A.ID, B.ID
# FROM TBL1 A FULL OUTER JOIN TBL2 B
# ON A.ID = B.ID
# (2)
# SELECT A.ID, B.ID
# FROM TBL1 A LEFT OUTER JOIN TBL2 B
# ON A.ID = B.ID
# UNION
# SELECT A.ID, B.ID
# FROM TBL1 A RIGHT OUTER JOIN TBL2 B
# ON A.ID = B.ID
# (3)
# SELECT A.ID, B.ID
# FROM TBL1 A, TBL2 B
# WHERE A.ID = B.ID
# UNION ALL
# SELECT A.ID, NULL
# FROM TBL1 A
# WHERE NOT EXISTS (SELECT 1 FROM TBL2 B WHERE A.ID = B.ID)
# UNION ALL
# SELECT NULL, B.ID
# FROM TBL2 B
# WHERE NOT EXISTS (SELECT 1 FROM TBL1 A WHERE B.ID = A.ID)
#
# 1. 1, 2
# 2. 1, 3
# 3. 2, 3
# 4. 1, 2, 3
#
# 답 4
#
# 아래의 EMP 테이블과 DEPT 테이블에서 밑줄 친 속성은 주키이며 EMP C는 DEPT와 연결된 외래키이
# 다. EMP 테이블과 DEPT 테이블은 LEFT, FULL, RIGHT 외부조인(outer join)하면 생성되는 결과 건수로
# 가장 적절한 것은? # 74
#
# 아래
# EMP 테이블
# A	B	C
# 1	b	w
# 3	d	w
# 5	y	y
#
# DEPT 테이블
# C	D	E
# w	1 	10
# z	4	11
# v	2	22
#
# 1. 3건, 5건, 4건
# 2. 4건, 5건, 3건
# 3. 3건, 4건, 4건
# 4. 3건, 4건, 5건
#
# 답 1
#
# 신규 부서의 경우 일시적으로 사원이 없는 경우도 있다고 가정하고 DEPT와 EMP를 조인하되 사원이
# 없는 부서 정보도 같이 출력하도록 할 때, 아래 SQL문장의 ㄱ 안에 들어갈 내용을 기술하시오. # 75
#
# 아래
# SELECT E.ENAME, D.DEPTNO, D.DNAME
# FROM DEPT D ㄱ EMP E
# ON D.DEPTNO = E.DEPTNO;
#
# 답 LEFT JOIN 또는 LEFT OUTER JOIN
#
# 다음 중 아래와 같은 데이터 상황에서 SQL의 수행 결과로 가장 적절한 것은? # 76
#
# 아래
# TAB
# C1	C2
# A	1
# B	2
# C	3
# D	4
# E	5
# TAB2
# C1	C2
# B	2
# C	3
# D	4
#
# SELECT*
# FROM TAB1 A LEFT OUTER JOIN TAB2 B
# ON (A.C1 = B.C1 AND B.C2 BETWEEN 1 AND 3)
#
# 1.
# C1	C2	C1	C2
# A	1
# B	2	B	2
# C	3	C	3
# D	4	D	4
# E	5
# 2.
# C1	C2	C1	C2
# A	1
# B	2	B	2
# C	3	C	3
# D	4
# E	5
# 3.
# C1	C2	C1	C2
# A	1
# B	2	B	2
# C	3	C	3
# 4.
# C1	C2	C1	C2
# A	1
# B	2	B	2
# C	3	C	3
# D	4	D	4
#
# 답 2
#
# 아래와 같은 데이터 모델에서 ORACLE을 기준으로 SQL을 작성하였다. 그러나 SQLSever에서도 동일
# 한 결과를 보장할 수 있도록 ANSI 구문으로 SQL을 변경하려고 한다. 다음 중 아래의 SQL을 ANSI 표준
# 구문으로 변경한 것으로 가장 적절한 것은? # 77
#
# 아래
# [SQL]
# SELECT A.게시판ID, A.게시판명, COUNT(B.게시글ID) AS CNT
# FROM 게시판 A, 게시글 B
# WHERE A.게시판ID = B.게시판ID(+)
# AND B.삭제여부(+) = 'N'
# AND A.사용여부 = 'Y'
# GROUP BY A.게시판ID, A.게시판명
# ORDER BY A.게시판ID;
#
# 1.
# SELECT A.게시판ID, A.게시판명, COUNT(B.게시글ID) AS CNT
# FROM 게시판 A LEFT OUTER JOIN  게시글 B
# ON (A.게시판ID = B.게시판ID AND B.삭제여부 = 'N')
# WHERE A.사용여부 = 'Y'
# GROUP BY A.게시판ID, A.게시판명
# ORDER BY A.게시판ID;
# 2.
# SELECT A.게시판ID, A.게시판명, COUNT(B.게시글ID) AS CNT
# FROM 게시판 A LEFT OUTER JOIN 게시글 B
# ON (A.게시판ID = B.게시판ID AND A.사용여부 ='Y')
# WHERE B.삭제여부 = 'N'
# GROUP BY A.게시판ID, A.게시판명
# ORDER BY A.게시판ID;
# 3.
# SELECT A.게시판ID, A.게시판명, COUNT(B.게시글ID) AS CNT
# FROM 게시판 A LEFT OUTER JOIN 게시글 B
# ON (A.게시판ID = B.게시판ID)
# WHERE A.사용여부 = 'Y'
# AND B.삭제여부 = 'N'
# GROUP BY A.게시판ID, A.게시판명
# ORDER BY A.게시판ID;
# 4.
# SELECT A.게시판ID, A.게시판명, COUNT(B.게시글ID) AS CNT
# FROM 게시판 A RIGHT OUTER JOIN 게시글 B
# ON (A.게시판ID = B.게시판ID AND A.사용여부 = 'Y' AND B.삭제여부 = 'N')
# GROUP BY A.게시판ID, A.게시판명
# ORDER BY A.게시판ID;
#
# 답  1
#
# 다음 과 같은 2개의 릴레이션이 있다고 가정하자.  student의 기본키는 st_num이고, department의
# 기본키는 dept_num이다. 또한 student의 d_num은 department의 dept_num을 참조하는 외래키이다.
# 아래 SQL문의 실행 결과 건수는? # 78
#
# 아래
# SELECT count(st_name)
# FROM student s
# WHERE not exists
# 	(SELECT *
# 	 FROM department d
# 	 WHERE s.d_num = d.dept_num
# 	 and dept_name = '전자계산학과');
#
# Student
# st_num	st_name	d_num
# 1001	Yoo	10
# 1002	Kim	30
# 1003	Lee	20
# 1004	Park	10
# 1005	Choi	20
# 1006	Jeong	10
#
# Department
# dept_num	dept_name
# 10		컴퓨터공학과
# 20		원자력공학과
# 30		전자계산학과
#
# 답 5
#
# (SQL Sever) 다음 중 아래의 SQL과 동일한 결과를 추출하는 SQL은? # 79
# (단, 테이블 TAB1, TAB2의 PK 컬럼은 A, B이다)
#
# 아래
# [SQL]
# SELECT A, B
# FROM TAB1
# EXCEPT
# SELECT A, B
# FROM TAB2;
#
# 1.
# SELECT TAB2.A TAB2.B
# 	FROM TAB1, TAB2
# 	WHERE TAB1.A ◇ TAB2.A
# 	AND TAB1.B ◇ TAB2.B
# 2.
# SELECT TAB1.A, TAB1.B
# 	FROM TAB1
# 	WHERE TAB1.A NOT IN (SELECT TAB2.A
# 		Q		FROM TAB2)
# 	AND TAB1.B NOT IN (SELECT TAB2.B
# 				FROM TAB2)
# 3.
# SELECT TAB2.A, TAB2.B
# 	FROM TAB1, TAB2
# 	WHERE TAB1.A = TAB2.A
# 	AND TAB1.B = TAB2.B
# 4.
# SELECT TAB1.A TAB1.B
# 	FROM TAB1
# 	WHERE NOT EXISTS (SELECT 'X'
# 				FROM TAB2
# 				WHERE TAB1.A = TAB2.A
# 				AND TAB1.B = TAB2.B);
#
# 답 4
#
# 아래와 같은 데이터 모델에 대해 SQL을 수행 하였다. 다음 중 수행된 SQL과 동일한 결과를 도출하는
# SQL은? # 80
#
# [수행 SQL]
# SELECT A.서비스ID, B.서비스명, B.서비스URL
# FROM (SELECT 서비스ID
# 	FROM 서비스,
# 		INTERSECT
# 		SELECT 서비스ID
# 		FROM 서비스이용) A, 서비스 B
# WHERE A.서비스ID = B.서비스ID;
#
# 1.
# SELECT B.서비스ID, A.서비스명, A.서비스URL
# FROM  서비스 A, 서비스이용 B
# WHERE A.서비스ID = B.서비스ID;
# 2.
# SELECT X.서비스ID, X.서비스명, X.서비스URL
# FROM 서비스 X
# WHERE NOT EXISTS (SELECT 1
# 			FROM (SELECT 서비스ID
# 				FROM 서비스
# 					MINUS
# 					SELECT 서비스ID
# 					FROM 서비스이용) Y
# 			WHERE X.서비스ID = Y.서비스ID);
# 3.
# SELECT B.서비스ID, A.서비스명, A.서비스URL
# FROM 서비스 A LEFT OUTER JOIN 서비스이용 B
# ON (A.서비스ID = B.서비스ID)
# WHERE B.서비스ID IS NULL
# GROUP BY B.서비스ID, A.서비스명, A.서비스URL;
# 4.
# SELECT A.서비스ID, A.서비스명, A.서비스URL
# FROM 서비스 A
# WHERE 서비스ID IN (SELECT 서비스ID
# 			FROM 서비스이용
# 			MINUS
# 				SELECT 서비스ID
# 				FROM 서비스);
#
# 답  2
