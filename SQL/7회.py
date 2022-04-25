# 다음 중 5개의 테이블로부터 필요한 칼럼을 조회하려고 할 때, 최소 몇개의 JOIN 조건이 필요한가?# 61
#
# 1. 2개
# 2. 3개
# 3. 4개
# 4. 5개
#
# 답 3
#
# 아래의 영화 데이터베이스 테이블의 일부에서 밑줄 친 속성들은 테이블의 기본키이며 출연료가 8888
# 이상인 영화명, 배우명, 출연료를 구하는 SQL로 가장 적절한 것은? # 62
#
# 아래
# 배우(배우번호, 배우명, 성별)
# 영화(영화번호, 영화명, 제작년도)
# 출연(배우번호, 영화번호, 출연료)
#
# 1.
# SELECT 출연.영화명, 영화.배우명, 출연.출연료
# FROM 배우, 영화, 출연
# WHERE 출연료 >= 8888
# AND 출연.영화번호 = 영화.영화번호
# AND 출연.배우번호 = 배우.배우번호;
# 2.
# SELECT 영화.영화명, 배우.배우명, 출연료
# FROM 영화, 배우, 출연
# WHERE 출연료 > 8888
# AND 출연.영화번호 = 영화.영화번호
# AND 영화.영화번호 = 배우.배우번호;
# 3.
# SELECT 영화명, 배우명, 출연료
# FROM 배우, 영화, 출연
# WHERE 출연료 >= 8888
# AND 영화번호 = 영화.영화번호
# AND 배우번호 = 배우.배우번호;
# 4.
# SELECT 영화.영화명, 배우.배우명, 출연료
# FROM 배우, 영화, 출연
# WHERE 출연료 >= 8888
# AND 출연.영화번호 = 영화.영화번호
# AND 출연.배우번호 = 배우.배우번호;
#
# 답 4
#
# 다음 중 아래에서 Join에 대한 설명으로 가장 적절한 것은? # 63
#
# 아래
# 가) 일반적으로 Join은 PK와 FK 값의 연관성에 의해 성립된다.
# 나) DBMS 옵티마이져는 From 절에 나열된 테일블들을 임의로 3개 정도씩 묶어서 Join을 처리한다.
# 다) EQUI Join은 Join에 관여하는 테이블 간의 컬럼 값들이 정확하게 일치하는 경우에 사용되는 방법이다.
# 라) EQUI Join은 '=' 연산자에 의해서만 수행되며, 그 이외의 비교연산자를 사용하는 경우에는 모두
# Non EQUI Join이다.
# 마) 대부분 Non EQUI Join을 수행할 수 있지만, 때로는 설계상의 이유로 수행이 불가능한 경우도 있다.
#
# 1. 가, 다, 라
# 2. 가, 나, 다
# 3. 가, 나, 다, 라
# 4. 가, 다, 라, 마
#
# 답 4
#
# 다음 SQL의 실행 결과로 맞는 것은? # 64
#
# 1. 0
# 2. 2
# 3. 4
# 4. 6
#
# 답 3
#
# 다음 중 순수 관계 연산자에 해당하지 않는 것은? # 65
#
# 1. SELECT
# 2. UPDATE
# 3. JOIN
# 4. DIVIDE
#
# 답 2
#
# 다음 중 아래 데이터 모델을 참고하여 설명에 맞게 올바르게 작성한 SQL문장을 2개 고르시오. # 66
#
# 아래
# [설명]
# 우리는 매일 배치작업을 통하여 고객에게 추천할 컨테츠를 생성하고 고객에게 추천서비스를 제공한다.
# 추천 컨텐츠 엔터티에서 언제 추천을 해야 하는지를 정의하는 추천 대상이자가 있어 해당일자에만
# 컨텐츠를 추천해야 한다. 또한 고객이 컨텐츠를 추천 받았을 때 선호하는 컨텐츠가 아닌 경우에는
# 고객이 비선호 컨텐츠로 분류하여 더 이상 추천 받기를 원하지 않는다. 그로므로 우리는 비선호 컨텐
# 츠 엔터티에 등록된 데이터에 대해서는 추천을 수행하지 않아야 한다.
#
# ※ 배치작업이란? 어떤 처리를 연속적으로 하는 것이 아니고 일정량씩 나누어 처리하는 경우 그 일정
# 량을 배치(batch)라고 한다. 배치의 원뜻은 한 묶음이라는 의미다. [기계공학용어사전]
# 예) 상품을 주문하는 로직은 그당시에 발생하는 트랜잭션에 대한 처리이므로 배치작이라 표현하지
# 않는다. 하지만 상품별 주문량을 집계하는 로직의 경우 특정조건(기간등)으로 일괄처리를 해야함으로
# 배치작업이라 표현할 수 있다.
#
# 1.
# SELECT C.컨텐츠ID, C.컨텐츠명
# FROM 고객 A INNER JOIN 추천컨텐츠 B
# ON (A.고객ID = B.고객ID) INNER JOIN 컨텐츠 C
# ON (B.컨텐츠ID = C.컨텐츠ID)
# WHERE A.고객ID = #custId#
# AND B.추천대상일자 = TO_CHAR(SYSDATE, 'YYYY.MM.DD')
# AND NOT EXISTS (SELECT X.컨텐츠ID
# 		FROM 비선호컨텐츠 X
# 			WHERE X.고객ID = B.고객ID);
# 2.
# SELECT C.컨텐츠ID, C.컨텐츠명
# FROM 고객 A INNER JOIN 추천컨텐츠 B
# ON (A.고객ID = #custId# AND A.고객ID = B.고객ID) INNER JOIN 컨텐츠 C
# ON (B.컨텐츠ID = C.컨텐츠ID) RIGHT OUTER JOIN 비선호컨텐츠 D
# ON (B.고객ID = D.고객ID AND B.컨텐츠ID = D.컨텐츠ID)
# WHERE B.추천대상일자 = TO_CHAR(SYSDATE, 'YYYY.MM.DD')
# AND B.컨텐츠ID IS NOT NULL;
# 3.
# SELECT C.컨텐츠ID, C.컨텐츠명
# FROM 고객 A INNER JOIN 추천컨텐츠 B
# ON (A.고객ID = B.고객ID) INNER JOIN 컨텐츠 C
# ON (B.컨텐츠ID = C.컨텐츠ID) LEFT OUTER JOIN 비선호컨텐츠 D
# ON (B.고객ID = D.고객ID AND B.컨텐츠ID = D.컨텐츠ID)
# WHERE A.고객ID = #custId#
# AND B.추천대상일자 = TO_CHAR(SYSDATE, 'YYYY.MM.DD')
# AND D.컨텐츠ID IS NULL;
# 4.
# SELECT C.컨텐츠ID, C.컨텐츠명
# FROM 고객 A INNER JOIN 추천컨텐츠 B
# ON (A.고객ID = #custId# AND A.고객ID = B.고객ID) INNER JOIN 컨텐츠 C
# ON (B.컨텐츠ID = C.컨텐츠ID)
# WHERE B.추천대상일자 = TO_CHAR(SYSDATE, 'YYYY.MM.DD')
# AND NOT EXISTS (SELECT X.컨텐츠ID
# 		FROM 비선호컨텐츠 X
# 			WHERE X.고객ID = B.고객ID
# 			AND X.컨텐츠ID = B.컨텐츠ID);
#
# 답 3, 4
#
# 아래는 어느 회사의 생산설비를 위한 데이터 모델의 일부에 대한 설명으로 가장 적절한 것을 2개
# 고르시오. # 67
#
# 1. 제품, 생산제품, 생산라인 엔터티를 Innere Join 하기 위해서 생산제품 엔터티는 WHERE절에 최소
# 2번이 나타나야 한다.
# 2. 제품과 생산라인 엔터티를 Join시 적절한 Join조건이 없으므로 카티시안 곱(Cartesian Product)이
# 발생한다.
# 3. 제품과 생산라인 엔터티에는 생산제품과 대응되지 않는 레코드는 없다.
# 4. 특정 생산라인번호에서 생산되는 제품의 제품명을 알기위해서 제품, 생산제품, 생산라인까지 3개
# 엔터티의 Inner Join인 필요하다.
#
# 답 1, 2
#
# 아래의 테이블 스키마 정보를 참고하여, 다음 중 '구매 이력이 있는 고객 중 구매 횟수가 3회 이상인
# 고객의 이름과 등급을 출력하시오.'라는 질의에 대해 아래 SQL 문장의 ㄱ,ㄴ에 들어 갈 구문으로 가장
# 적절한 것은? # 68
#
# 아래
# [SQL 문장]
# SELECT A.이름, A.등금
# FROM 고객 A
# ㄱ
# GROUP BY A.이름, A.등급
# ㄴ
#
# 1.
# ㄱ: INNER JOIN 구매정보 B ON A.고객번호=B.고객번호
# ㄴ: HAVING SUM(B.구매번호) >= 3
# 2.
# ㄱ: INNER JOIN 구매정보 B ON A.고객번호=B.고객번호
# ㄴ: HAVING COUNT(B.구매번호) >= 3
# 3.
# ㄱ: LEFT OUTER JOIN 구매정보 B ON A.고객번호=B.고객번호
# ㄴ: HAVING SUM(B.구매번호) >= 3
# 4.
# ㄱ: INNER JOIN 구매정보 B ON A.고객번호=B.고객번호
# ㄴ: WHERE B.구매번호 >= 3
#
# 답 2
#
# 아래는 어느, 회사의 정산 데이터 모델의 일부이며 고객이 서비스를 사용한 시간대에 따라 차등 단가를
# 적용하려고 한다. 다음 중 시간대별사용량 테이블을 기반으로 고객별 사용금액을 추출하는 SQL으로
# 가장 적절한 것은? # 69
#
# 1.
# SELECT A.고객ID, A.고객명, SUM(B.사용량*C.단가) AS 사용금액
# FROM 고객 A INNER JOIN 시간대별사용량 B
# ON (A.고객ID = B.고객ID) INNER JOIN 시간대구간 C
# ON (B.사용시간대 <= C.시작시간대 AND B.사용시간대 >= C.종료시간대)
# GROUP BY A.고객ID, A.고객명
# ORDER BY A.고객ID, A.고객명;
# 2.
# SELECT A.고객ID, A.고객명, SUM(B.사용량*C.단가) AS 사용금액
# FROM 고객 A INNER JOIN 시간대별사용량 B INNER JOIN 시간대구간 C
# ON (A.고객ID = B.고객ID AND C.종료시간대
#       BETWEEN C.시작시간대 AND C.종료시간대)
# GROUP BY A.고객ID, A.고객명
# ORDER BY A.고객ID, A.고객명;
# 3.
# SELECT A.고객ID, A.고객명, SUM(B.사용량*C.단가) AS 사용금액
# FROM 고객 A INNER JOIN 시간대별사용량 B
# ON (A.고객ID = B.고객ID) INNER JOIN 시간대구간 C
# ON B.사용시간대 BETWEEN C.시작시간대 AND C.종료시간대
# GROUP BY A.고객ID, A.고객명
# ORDER BY A.고객ID, A.고객명;
# 4.
# SELECT A.고객ID, A.고객명, SUM(B.사용량*C.단가) AS 사용금액
# FROM 고객 A INNER JOIN 시간대별사용량 B
# ON (A.고객ID = B.고객ID) BETWEEN JOIN 시간대구간 C
# GROUP BY A.고객ID, A.고객명
# ORDER BY A.고객ID, A.고객명;
#
# 답 3
#
# 다음 중 팀(TEAM) 테이블과 구장(STADIUM) 테이블의 관계를 이용해서 소속팀이 가지고 있는 전용
# 구장의 정보를 팀의 정보와 함께 출력하는 SQL을 작성할 때 결과가 다른 것은? # 70
#
# 1. SELECT T. REGION_NAME, T.TEAM_NAME, T.STADIUM_ID, S.STADIUM_NAME
# 	FROM TEAM T INNER JOIN STADIUM S
# 		USING (T.STADIUM_ID = S.STADIUIM_ID);
# 2. SELECT TEAM.REGION_NAME, TEAM.TREAM_NAME, TEAM.STADIUM_ID,
# STADIUM.STADIUM_NAME
# 	FROM TEAM INNER JOIN STADIUM
# 		ON (TEAM.STADIUM_ID =
# STADIUM.STADIUM_ID)
# 3. SELECT T.REGION_NAME, T.TEAM_NAME, T.STADIUM_ID, S.STADIUM_NAME
# 	FROM TEAM T, STADIUM S
# 	WHERE T.STADIUM_ID = S.STADIUM_ID
# 4.
# SELECT TEAM.REGION_NAME, TEAM.TEAM_NAME, TEAM.STADIUM_ID, STADIUM.STADIUM_NAME
# 	FROM TEAM, STADIUM
# 	WHERE TEAM.STADIUM_ID = STADIUM.STADIUM_ID;
#
# 답 1

