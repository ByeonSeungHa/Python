import random
from PIL import Image

count = 0
fail = []
TOTAL = [
    ["다음 중 데이터에 양을 측정하는 바이트의 크기로 잘못 연결된 것은 무엇인가?" ,  #1
    [["킬로바이트(KB) : 10**3 Byte"],
    ["페타바이트(PB) : 10**15 Byte"],
    ["테라파이트(TB) : 10**12 Byte"],
    ["메가바이트(MB) : 10**9 Byte"]],[4]],

    ["다음이 설명하는 개념으로 적합한 용어는 무엇인가?\n"
     "개인이 정보 관리의 주체가 되어 능동적으로 본인의 정보를 관리하고, 본인의 의지에 따라 신용 및 자산관리 등에 정보를\n"
     "활용하는 일련의 과정이다.",  # 2
     [["YourData"],
      ["MyData"],
      ["OurData"],
      ["ItsData"]], [2]],

    ["다음 중 데이터 거버넌스의 구성요소로 올바르지 않은 것은?",  # 3
     [["원칙"],
      ["플랫폼"],
      ["조직"],
      ["프로세스"]], [2]],
    ["다음 중 다음 그림과 같은 빅데이터 조직 구조로 가장 적절한 것은 무엇인가?",  # 4
     [["집중구조"],
      ["기능구조"],
          ["분산구조"],
          ["협업구조"]], [2],1],
        ["다음이 설명하는 개인정보 비식별화 절차는 어떤 단계에 속하는가?\n"
         "비식별 정보 안전조치, 재식별 가능성 모니터링 등 비식별 정보 활용 과정에서 재식별 방지를 위해 필요한 조치 수행" ,  #5
    [["사전검토"],
    ["비식별 조치"],
    ["적정성 평가"],
    ["사후관리"]] ,[4]],

    ["다음이 설명하는 CRISP-DM 분석 방법론의 절차는 무엇인가?\n\n"
     "-분석을 위한 데이터를 수집 및 속성을 이해하고, 문제점을 식별하며 숨겨져있는 인사이트를 발겨하는 단계\n"
     "-초기 대이터 수집, 데이터 기술 분석, 데이터 탐색, 데이터 품질 확인",  # 6
     [["업무이해(Business Understanding)"],
      ["데이터 이해(Data Understanding)"],
      ["데이터 준비(Data Preparation)"],
      ["모델링(Modeling)"]], [2]],

    ["다음 중 아래에서 설명하는 프라이버시 보호 모델은 무엇인가?\n\n"
     "-동질성 공격, 배경 지식에 의한 공격을 방어하기 위한 프라이버시 모델이다.\n"
     "-주어진 데이터 집합에서 함께 비식별 되는 레코드들은(동질 집합에서) 적어도 몇개의 서로다른 민감한 정보를 가져와야 하는 프라이버시 모델이다.\n"
     "-비식별 조치 과정에서 충분히 다양한 서로 다른 민감한 정보를 갖도록 동질 집합을 구성한다.",# 7
     [["k-익명성"],
      ["l-다양성"],
      ["m-유일성"],
      ["t-근접성"]], [2]],

  ["다음 중 개인정보 비식별 조치 방법으로 가장 적절한 것은 무엇인가?\n\n"
   "-조치 전 : 주민등록번호 901212-1234567\n"
   "-조치 후 : 90년대 생, 남자",  # 8
     [["가명처리"],
      ["총계처리"],
      ["데이터 삭제"],
      ["데이터 마스킹"]], [3]],

    ["다음 중 분석 로드맵 단계로 가장 적절한 것은 무엇인가?", #9
    [["데이터 분석체계 도입 -> 데이터 분석 유효성 검증 -> 데이터 분석 확산 및 고도화"],
    ["데이터 분석체계 도입 -> 데이터 분석 확산 및 고도화 -> 데이터 분석 유효성 검증"],
    ["데이터 분석 유효성 검증 -> 데이터 분석 확산 및 고도화 -> 데이터 분석체계 도입"],
    ["데이터 분석 유효성 검증 -> 데이터 분석체계 도입 -> 데이터 분석 확산 및 고도화"]], [1]],

    ["다음 중 분석의 대상이 명확하게 무엇인지 모르는 경우 기존 분석 방식을 활용하여 새로운 지식을 도출하는 것으로 가장 적절한 것은 무엇인가?",  # 10
     [["최적화(Optimization)"],
      ["솔루션(Solution)"],
      ["통찰(Insight)"],
      ["발견(Discovery)"]], [3]],

    ["빅데이터 3V(Volume, Variety, Velocity)의 특징에 해당하지 않는 것은 ?",  # 11
     [["가치(Value)"],
      ["다양성(Variety)"],
      ["속도(Velocity)"],
      ["규모(Volumne)"]], [1]],
    ["다음 중 분석과제 우선순위 선정 매트릭스에서 분석 과제 적용 우선순위를 \"난이도\"에 둘 때 가장 올바른 우선 순위는 ?",  # 12
     [["III -> I -> II"],
      ["III -> IV -> II"],
      ["III -> II -> IV"],
      ["III -> II -> I"]], [1],1],
    ["다음 중 CRISP-DM 분석 방법론 단계로 올바른 것은 ?",  # 13
     [["데이터 이해 -> 데이터 준비 -> 업무 이해 -> 모델링 -> 평가 -> 전개"],
      ["업무 이해 -> 데이터 이해 -> 데이터 준비 -> 모델링 -> 평가 -> 전개"],
      ["데이터 이해 -> 데이터 준비 -> 업무 이해 -> 모델링 -> 전개 -> 평가"],
      ["업무 이해 -> 데이터 이해 -> 데이터 준비 -> 모델링 -> 전개 -> 평가"]], [2]],

    ["개인정보를 제공하기 위해 정보주체의 동의를 받을 때 고지 사항으로 올바르지 않은 것은 ?",  # 14
     [["개인정보의 수집 . 이용 목적"],
      ["개인정보에 대한 암호화 여부 및 안전성 확보 조치 여부"],
      ["개인정보를 제공받는 자"],
      ["수집하려는 개인정보의 항목 "]], [2]],

    ["다음 중 반정형 데이터로 가장 부적절한 것은 무엇인가 ? ",  # 15

     [["XML"],
      ["JSON"],
      ["HTML"],
      ["오디오"]], [4]],

    ["다음 중 데이터로부터 잡음을 제거하기 위해 데이터 추세에 벗어나는 값들을 변환하는 기법으로\n"
     "구간화, 군집화 등의 기법을 적용하는 데이터 변환 기술은 무엇인가?",  # 16
     [["정규화"],
      ["평활화"],
      ["집계"],
      ["일반화"]], [2]],

    ["다음 중 빅데이터 위기 요인의 통제 방안에 대한 설명으로 가장 옳지 않은 것은? ",  # 17
     [["개인정보 유출 및 사용으로 발생하는 피해에 대해 사용자가 책임을 지게한다."],
      ["예측 알고리즘을 통해 범죄를 일으킬 가능성이 있는 사람에 대하여 사전에 구속, 접근 금지 등의 조치를 취한다."],
      ["예측 알고리즘의 부당함을 반증할 수 있도록 알고리즘에 대한 접근권을 제공한다."],
      ["알고리즈미스트를 통하여 불이익을 당한 사람들을 대변한다."]], [2]],

["다음 중에서 암묵지와 형식지 간의 4단계 지식 전환 단계를 순서대로 가장 바르게 나타낸 것은 무엇인가? "
     " 다음 중 실시간 데이터로 가장 부적절한 것은 무엇인가?",  # 18
     [["공통화 -> 표출화 -> 연결화 -> 내면화"],
      ["내면화 -> 연결화 -> 공통화 -> 표출화"],
      ["표출화 -> 공통화 -> 연결화 -> 내면화"],
      ["연결화 -> 표출화 -> 공통화 -> 내면화"]], [1]],

    ["상향식 접근 방식(Bottom Up Approach)으로서 시행 착오를 통한 문제 해결을 위해 사용되며 가설의 생성(Hypotheses),\n"
     "디자인에 대한 실험(Design Experiments), 실제 환경에서의 테스트(Test), 테스트 결과에서의 통찰(Insight) 도출 및 가설 확인의 프로세스로 구성되는 접근법은\n"
     "다음 중 무엇인가? 1",  # 19
     [["프로토타이핑(Prototyping)"],
      ["최적화(Optimization)"],
      ["디자인 사고(Design Thinking)"],
      ["지도학습(Supervised Learning)"]], [1]],

    ["개인정보가 유출되었음을 알게 되었을 때에 개인정보처리자가 지체 없이 해당 정보주체에게 알려야 하는 사실로 올바르지 않은 것은? ",  # 20
     [["유출된 개인정보의 항목"],
      ["유출로 인하여 발생할 수 있는 피해를 최소화하기 위하여 정보주체가 할 수 있는 방법 등에 관한 정보"],
      ["개인정보처리자의 대응조치 및 피해 구제절차"],
      ["개인정보 유출 사고의 실시간 수사 진행 상황"]], [4]],

    ["다음 중 실시간으로 발생하는 이벤트 처리에 대한 결과값을 수집하고 처리하는 기술은 무엇인가?",  # 21
         [["CEP"],
          ["맵리듀스"],
          ["ETL"],
          ["피그"]], [1]],
    ["다음 중 불완전 자료는 모두 무시하고 완전하게 관측된 자료만 사용하여 분석하는 방법으로 가장 적절한 것은 무엇인가?",  # 22
     [["평균 대치법"],
      ["핫덱(Hot-Deck) 대체"],
      ["완전 분석법"],
      ["다중 대치법"]], [3]],

    ["다음 중 데이터값을 몇 개의 버킷으로 분할하여 계산하는 방법은 무엇인가?",  # 23
     [["단순 기능 변환"],
      ["정규화"],
      ["로그 변환"],
      ["비닝"]], [4]],

    ["다음 중 특정 모델링 기법에 의존하지 않고 데이터의 통계적 특성으로부터 변수를 택하는 기법으로 적절한 것은 무엇인가?",  # 24
     [["필터 기법"],
      ["임베디드 기법"],
      ["라쏘"],
      ["릿지"]], [1]],

["다음 중 변수들의 공분산 행렬이나 상관행렬을 이용하고 원래 데이터 특징을 잘 설명해주는 성분을 추출하기 위하여 고차원 공간의 표본들을 \n"
 "선형 연관성이 없는 저차원 공간으로 변환하는 기법으로 가장 적절한 것은?",  # 25
     [["주성분 분석"],
      ["특이값 분해"],
      ["상관 분석"],
      ["다차원 척도법"]], [1]],

    ["다수 클래스에 밀집된 데이터가 없을 때까지 데이터를 제거하여 데이터 분포에서 대표적인 데이터만 남도록 하는 방법으로 가장 적절한 것은 ?",  # 26
     [["랜덤 과소 표집(Random Under-Sampling)"],
      ["토멕 링크 방법(Tomek Link Method)"],
      ["CNN(Condensed Nearest Neighbor)"],
      ["ENN(Edited Nearest Neighbours)"]], [3]],
    ["포아송 분포에서 사건 발생 확률이 λ이고, 사건이 일어나는 횟수를 n이라고 할 때, 기대값과 분산은 얼마인가? ",  # 27
     [["기대값 : λ, 분산 : λ"],
      ["기대값 : 1/λ, 분산 : np"],
      ["기대값 : λ, 분산 : np"],
      ["기대값 : 1/λ, 분산 : λ"]], [1]],

    ["다음 중 다수 클래스의 데이터를 일부만 선택하여 데이터의 비율을 맞추는 방법은 무엇인가 ?",  # 28
     [["앙상블 기법"],
      ["과대 표집"],
      ["과소 표집"],
      ["임계값 이동 "]], [3]],

    ["다음 중 변수의 속성에 따른 분석 방법에 대한 설명 중 올바르지 않은 것은 ?",  # 29
     [["수치로 표현을 할 수 있는 측정 가능한 데이터 변수는 피어슨(Pearson) 상관계수를 통해서 분석한다."],
      ["데이터의 순서에 의미를 부여한 데이터 변수는 T-분포를 통해서 분석한다."],
      ["명목적 데이터는 카이제곱 검정을 통해서 분석한다."],
      ["데이터에 대한 분류의 의미를 지닌 명목적 데이터 변수 사이의 상관계수를 계산하는 것은 큰 의미가 없다."]], [2]],

    ["확률 변수 X와 질량 함수 P(X)가 다음과 같이 주어질 때, 확률 변수 X의 기댓값은 얼마인가?",  # 30
     [["1"],
      ["4/3"],
      ["5/3"],
      ["8/3"]], [4],1],
    ["다음 데이터 중 최빈수으로 가장 적절한 것은 무엇인가?\n"
     "[3,5,6,4,5]",  # 31
     [["3"],
      ["4"],
      ["5"],
      ["6"]], [3]],

    ["컴퓨터를 소유하고 있는 집단 A는 전체 학생의 80%이고, 그중에 50%가 League Of Legend를 플레이 해본 적이 있다.\n"
     "컴퓨터를 소유하고 있지 않은 집단 B는 전체학생의 20% 이고, 그중에 20% 학생이 League Of Legend를 플레이해본 적이 있다.\n"
     "League Of Legend를 플레이해본 학생을 임의로 선택했을 때 학생이 컴퓨터를 소유하지 않는 집단 B에 속할 확률은 얼마인가? ",  # 32
     [["1/3"],
      ["1/5"],
      ["1/11"],
      ["3/4"]], [3]],

    ["크기가 100인 표본으로 95% 신뢰수준을 가지도록 모평균을 추정하였는데, 신뢰구간의 길이가 20이었다. 동일한 조건에서 크기가 400인 표본으로\n"
     "95% 신뢰수준을 가지도록 모평균을 추정할 경우에 표본의 길이는 얼마인가?",  # 33
     [["10"],
      ["20"],
      ["40"],
      ["80"]], [1]],
    ["다음 일변량 데이터 탐색 방법으로 가장 알맞은 것은 무엇인가? ",  # 34
     [["기술 통계량"],
      ["산점도 행렬"],
      ["별 그림"],
      ["등고선 그림"]], [1]],
    ["다음 중 확률변수의 분산에 대한 성질로서 바르지 않은 것은? (단, X, Y는 확률변수이고 서로독립이며, a는 상수이다.) ",  # 35
     [["V( X - Y ) = V(X) - V(Y)"],
      ["V(a) = 0"],
      ["V(aX) =a**2V(X)"],
      ["V( X + Y ) = V(X) + V(Y)"]], [1]],

    ["다음 중 제1종 오류를 범할 최대 허용확률을 의미하는 용어는 무엇인가? ",  # 36
     [["신뢰수준(Level of Confidence)"],
      ["유의수준(Level of Significance)"],
      ["베타수준"],
      ["검정력"]], [2]],

    ["평균이 10이고 분산이 25인 정규 모집단에서 크기가 9인 표본을 추출하였을 경우 표본평균의 표준편차는 얼마인가? ",  # 37
     [["5/2"],
      ["5/3"],
      ["25/9"],
      ["10/9"]], [2]],

    ["다음 중 모집단이 정규 분포라는 정도만 알고, 모 표준편차는 모를 때 사용하는 분포로 가장 알맞은 것은 무엇인가? ",  # 38
     [["정규 분포"],
      ["F - 분포"],
      ["T - 분포"],
      ["X(카이)제곱- 분포"]], [3]],
    ["동전을 세번 던졌을 때 앞면이 한 번 나올 확률은 얼마인가?",  # 39
     [["0.125"],
      ["0.375"],
      ["0.5"],
      ["0.625"]], [2]],

    ["고등학교 남학생의 키를 추정하기 위하여 100명을 임의로 선택하여 평균 키를 측정하였더니 175cm, 분산은 25였다.\n"
     "고등학교 남학생의 평균 키에 대한 95% 신뢰구간은 다음 중 무엇인가? (단, Z0.025 = 1.96, Z0.05 = 1.645)",  # 40
     [["174.18 <= u <= 175.82"],
      ["174.02 <= u <= 175.98"],
      ["173.36 <= u <= 176.65"],
      ["173.04 <= u <= 176.96"]], [2]],

    ["다음 중에서 의사결정나무의 알고리즘에 대한 설명으로 가장 옳지 않은 것은?",  # 41
     [["CART는 목적변수가 이산형일 경우에 불순도의 측도로 엔트로피 지수를 이용한다."],
      ["C4.5와 C5.0은 각 마디에서 다지 분리(Multiple Split)가 가능하다."],
      ["CHAID에서는 불순도의 측도로 카이제곱 통계량을 이용한다."],
      ["QUEST에서 분리규칙은 분리변수 선택과 분리점 선택의 두 단계로 나누어 시행한다."]], [1]],

    ["다음 중 매개변수(Parameter)의 예시로 가장 알맞지 않은 것은?",  # 42
         [["신경망 학습에서 학습률(Learning Rate)"],
          ["인공신경망에서의 가중치"],
          ["서포트 벡터 머신에서의 서포트 벡터"],
          ["선형 회귀나 로지스틱 회귀 분석에서의 결정계수"]], [1]],

    ["다음 중 분석 모형 구축 절차 중 요건 정의에 따라 상세 분석 기법을 적용해 모델을 개발하는 과정으로 가장 적합한 것은 무엇인가?",  # 43
     [["요건 정의"],
      ["모델링"],
      ["적용"],
      ["검증 및 테스트"]], [2]],

    ["다음 중 R과 거의 같은 작업 수행이 가능한 C언어 기반의 오픈 소스 프로그래밍 언어는 무엇인가? ",  # 44
         [["R-Studio"],
          ["S-PLUS"],
          ["파이썬"],
          ["JAVA"]], [3]],

    ["다음 중 데이터 분할에 대한 설명으로 가장 알맞지 않은 것은?",  # 45
     [["데이터 분할은 데이터를 훈련 데이터, 검증 데이터, 평가 데이터로 분할하는 작업이다."],
      ["데이터 분할을 하는 이유는 모형이 주어진 데이터에 대해서만 높은 성능을 보이는 과대 적합의 문제를 예방하여 1종 오류인 잘못된 귀무가설을\n"
       "채택하는 오류를 방지하는 데 목적이 있다."],
      ["훈련 데이터와 검증 데이터는 학습 과정에서 사용하며 평가 데이터는 학습 과정에 사용되지 않고 오로지 모형의 평가를 위한 과정에만 사용된다."],
      ["검증 데이터를 사용하여 모형의 학습 과정에서 모형이 제대로 학습되었는지 중간에 검증을 실시하고, 과대 적합과 과소 적합의 발생 여부 등을\n"
       "확인하여 모형의 튜닝에도 사용한다."]], [2]],

    ["다음 중 다중회귀 모형의 수식으로 가장 알맞은 것은",  # 46
     [["1"],
      ["2"],
      ["3"],
      ["4"]], [2],1],

    ["다음 중 로지스틱 회귀 분석에 대한 설명으로 가장 알맞지 않은 것은?",  # 47
     [["반응변수가 범주형인 경우 적용되는 회귀 분석 모형이다."],
      ["새로운 설명변수의 값이 주어질 때 반응변수의 각 범주에 속할 확률이 얼마인지를 추정하여 추적 확률을 기준치에 따라 분류하는 목적으로 사용될 수 있다."],
      ["승산비는 1-p/p로 계산한다."],
      ["R을 사용하여 로지스틱 회귀 분석을 수행하고 결과를 해석할 수 있다."]], [3]],

    ["다음 중 의사결정나무의 분석 과정으로 가장 알맞은 것은 무엇인가?",  # 48
     [["의사결정나무 성장 -> 가지치기 -> 타당성 평가 -> 해석 및 예측"],
      ["의사결정나무 성장 -> 타당성 평가 -> 가지치기 -> 해석 및 예측"],
      ["타당성 평가 -> 가지치기 -> 의사결정나무 성장 -> 해석 및 예측"],
      ["타당성 평가 -> 의사결정나무 성장 -> 가지치기 -> 해석 및 예측"]], [1]],


    ["다음 중 시간이 지날수록 관측치의 평균값이 지속적으로 증가하거나 감소하는 시계열 모형으로 가장 알 맞은 것은 ?",  # 49
     [["자기 회귀 모형"],
      ["이동평균 모형"],
      ["백색잡음"],
      ["분해 시계열"]], [2]],


    ["다음 중 서포트 벡터 머신의 구성요소로 가장 알맞지 않은 것은 ?",  # 50
     [["초평면"],
      ["활성화 함수"],
      ["서포트 벡터"],
      ["슬랙 변수"]], [2]],

["다음은 수제비 쇼핑몰의 거래내역이다. 연관 규칙 \"커피->빵\"에 대한 지지도(support)는 얼마인가?",  # 51
     [["3/5"],
      ["1/3"],
      ["1/2"],
      ["2/5"]], [3],1],

    ["다음 중 아래 그림과 같이 군집 내의 오차 제곱합(Error Sum of Square)에 기초하여 군집을 수행하는 기법은 무엇인가?",  # 52
     [["최장연결법"],
      ["중심연결법"],
      ["평균연결법"],
      ["와드연결법"]], [4],1],

["데이터 분석 모형을 정의할 때 모델 내부에서 확인이 가능한 변수로 데이터를 통해서 산출이 가능한 값은 무엇인가?",  # 53
     [["매개변수(Parameter)"],
      ["편향(Bias)"],
      ["신경망 학습에서 학습률(Learning Rate)"],
      ["KNN에서의 K의 개수"]], [1]],

    ["다음이 설명하는 의사결정나무 분석 과정 단계는 무엇인가?\n"
     "-분석 목적과 자료구조에 따라 적절한 분리 규칙(Spliting Rule) 및 정지 규칙(Stopping Rule)을 지정함 ",  # 54
     [["의사결정나무 성장(Growing)"],
      ["가지치기(Pruning)"],
      ["해석 및 예측"],
      ["타당성 평가"]], [1]],

    ["다음중 입력층과 출력층으로만 구성된 최초의 인속 신경망은 무엇인가?",  # 55
     [["퍼셉트론(Perceptron)"],
      ["순방향 신경망(Feed Forward Neural Network)"],
      ["합성곱 신경망(Convolutional Neural Network)"],
      ["다층 퍼셉트론(Multi-Layer Perceptrons; MLP)"]], [1]],

    ["다음 중 활성화 함수로 옳지 않은 것은",  # 56
     [["계단함수"],
      ["시그모이드 함수"],
      ["ReLU 함수"],
      ["우도 함수"]], [4]],

    ["다음에서 설명하는 변수 거리의 측정 방법은 무엇인가?\n"
     "명목형 변수의 거리 측정 방법\n"
     "-두 집합 사이의 유사도를 측정하는 방법\n"
     "-9과 1 사이의 값을 가지며 두 집합이 동일하면 1의 값, 공통의 원소가 하나도 없으면 0의 값을 가짐",  # 57
     [["단순 일치계수"],
      ["자카드 계수"],
      ["순위 상관계수"],
      ["맨하튼 거리"]], [2]],

    ["다음 중 텍스트 형태로 이루어진 비정형 데이터들을 자연어 처리 방식을 이용해 정보를 추출하는 기법으로 가장 알맞은 것은 무엇인가?",  # 58
     [["배깅(Bagging)"],
      ["서포트 백터 머신(SVM)"],
      ["ADASYN"],
      ["텍스트 마이닝(Text Mining)"]], [4]],

    ["다음 중 서포트 벡터 머신(SVM)에 대한 설명으로 옳지 않은 것은?",  # 59
     [["서포트 벡터 머신에서 서포트 벡터는 여러 개 일 수도 있다."],
      ["서포트 벡터 머신은 기계학습의 한 분야로 사물인식, 패턴 인식, 손 글씨 숫자 인식 등 다양한 분야에서 활용되고 있는 지도 학습 모델이다."],
      ["최대 마진(Margin: 여유공간)을 가지는 비확률적 선형 판별에 기초한 이진 분류기이다."],
      ["SVM은 훈련 시간이 상대적으로 빠르지만, 정확성이 낮고 다른 방법보다 과대 적합의 가능성이 높은 모델이다."]], [4]],

    ["다음 중 잘못 분류된 개체들에 가중치를 적용, 새로운 분류 규칙을 만들고, 이 과정을 반복해 최종 모형을 만드는 알고리즘으로 가장 알맞은 것은?",  # 60
     [["배깅(Bagging)"],
      ["보팅(Voting)"],
      ["랜덤 포레스트(Random Forest)"],
      ["부스팅(Boosting)"]], [4]],

    ["다음 예측값과 실젯값이 차이의 제곱합으로 가장 알맞은 것은?",  # 61
     [["SSE"],
      ["SST"],
      ["SSR"],
      ["AE"]], [1]],

    ["다음 중 데이터 분석 모형의 오류에 대한 설명으로 가장 알맞지 않은 것은?",  # 62
     [["일반화 오류는 분산 모형을 만들 때 주어진 데이터 집합의 특성을 지나치게 반영하여 발생하는 오류이다."],
      ["일반화 오류는 과소 적합되었다고 한다."],
      ["일반화 오류는 주어진 데이터 집합은 모집단 일부분임에도 불구하고 그것이 가지고 있는 주변적인 특성, 단순 잡음 등을 모두 묘사하기 때문에\n"
       "     일반화 오류가 발생한다."],
      ["학습오류는 주어진 데이터 집합에 부차적인 특성과 잡음이 있다는 점을 고려하여 그것의 특성을 덜 반영하도록 분석모형을 만들어 생기는 오류이다."]], [2]],

    ["데이터 집합을 무작위로 동일 크기를 갖는 K개의 부분 집합으로 나누고, 그중 1개 부분 집합을 평가 데이터(Test Set)로, 나머지 (K-1)개의\n"
     "부분 집합을 훈련 데이터(Training Set)로 선정하여 분석 모형을 평가하는 기법으로 가장 알맞은 것은?",  # 63
     [["랜덤 서브샘플링(Ramdom Sub-Sampling)"],
      ["K-fold Cross Validation"],
      ["홀드 아웃(Holdout)"],
      ["LOOCV"]], [2]],

    ["다음 중 범주에 따라 분류된 변수가 정규 분포되어 있다면 빈도가 실제 기대되는 값으로 부터 유의미한 차이가 관찰되는가를 보기 위한 검증으로\n"
     "가장 알맞은 것은?",  # 64
     [["Z-검정"],
      ["카이제곱 검정"],
      ["분산 분석"],
      ["T-검정"]], [2]],

    ["다음 적합도 검정 방법 중에서 정규성 검정에 사용되지 않는 검정 방법은?",  # 65
     [["샤피로-윌크 검정"],
      ["콜모고로프-스미르노프 적합성 검정"],
      ["카이제곱 검정"],
      ["Q-Q Plot"]], [3]],


    ["다음 중 과대 적합을 방지하는 방법으로 가장 알맞지 않은 것은 ?",  # 76
     [["데이터 세트 감소"],
      ["모델 복잡도 감소"],
      ["가중치 규제"],
      ["드롭아웃"]], [1]],

    ["매개변수 중 하나의 뉴런에 입력된 모든 값을 다 더한값(가중합)에 더해주는 상수는 무엇인가 ?",  # 77
         [["손실 함수 "],
          ["가중치"],
          ["학습률"],
          ["편향"]], [4]],

    ["다음 중 훈련 데이터를 중복하여 사용하지 않고 훈련 데이터 세트를 나누는 기법으로 가장 알맞은 것은?",  # 78
     [["직접 투표"],
      ["배깅"],
      ["페이스팅"],
      ["랜덤 서브스페이스"]], [3]],

    ["다음 중 경사하강법을 이용하여 가중치 업데이트하여 최적화된 결과를 얻는 기법은 무엇인가?",  # 79
     [["랜덤 패치"],
      ["랜덤 포레스트"],
      ["에이다 부스트"],
      ["그레디언트 부스트"]], [4]],

    ["다음 중 관계 시각화 기법으로 가장 알맞지 않은 것은?",  # 70
     [["산점도"],
      ["도넛 차트"],
      ["버블 차트"],
      ["히스토그램"]], [2]],

    ["다음 중 하나의 자산을 획득하려 할 때 주어진 기간 동안 모든 연관 비용을 고려할 수 있도록 확인하기 위해 사용되는 평가 기법으로 가장 알맞은 것은?",  # 71
     [["TCO"],
      ["ROI"],
      ["NPV"],
      ["IRR"]], [1]],

    ["다음 중 막대를 사용하여 전체 비율을 보여주면서 여러 가지 범주를 동시에 차트로 표현 가능한 그래프로 가장 알맞은 것은 무엇인가? ",  # 72
     [["막대그래프"],
      ["선 그래프"],
      ["영역 차트"],
      ["누적 막대그래프"]], [4],1],

    ["다음 중 관계 시각화에 대한 설명으로 가장 알맞지 않은 것은? ",  # 73
     [["다변량 데이터 사이에 존재하는 변수 사이의 연관성, 분포와 패턴을 찾는 시각화 방법이다."],
      ["변수 사이의 연관성인 상관관계는 한 가지 요소의 변화가 다른 요소의 변화와 관련이 있는지를 표현하는 시각화 기법이다."],
      ["산점도 행렬은 산점도에서 데이터값을 나타내는 점 또는 마크에 여러가지 의미를 부여하여 확장된 차트이다."],
      ["관계 시각화의 유형으로 산점도, 산점도 행렬, 버블 차트, 히스토그램 등이 있다."]], [3]],

    ["다음 중 여러 가지 변수를 비교할 수 있는 시각화 그래프로 가장 알맞은 것은?",  # 74
     [["히트맵"],
      ["플로팅 바 차트"],
      ["체르토프 페이스"],
      ["스타 차트"]], [1],1],

    ["다음 중 인포그래픽 유형으로 가장 알맞지 않은 것은?",  # 75

     [["지도형은 특정 국가나 지역의 지도 안에 정보를 담는 방식이다."],
      ["스토리텔링형은 캐릭터 등의 만화적 요소를 활용한 방식이다."],
      ["도표형은 다양한 표와 그래프를 사용해 정보를 담는 방식이다."],
      ["타임라인형은 주제를 선정하여 관련된 히스토리를 타임라인 형태로 나타내는 방식이다."]], [2]],

    ["다음 혼동 행렬(Confusion Matrix)에서 특이도(Specificity)와 정밀도(Precision)는 무엇인가",  # 76
     [["특이도: 3/4, 정밀도: 2/4"],
      ["특이도: 3/4, 정밀도: 1/4"],
      ["특이도: 1/4, 정밀도: 3/4"],
      ["특이도: 1/4, 정밀도: 2/4"]], [2],1],

    ["초기 아이디어 개발 관점 분류 중 생각하고 있는 것, 기억하고 있는 내용을 마음속에 지도를 그리듯이 줄거리를 이해하며 정리하는 방법으로 가장 알맞은 것은?",  # 77
         [["친화 도표 방식"],
          ["마인드맵 방식"],
          ["피라미드 방식"],
          ["평행 좌표 그래프"]], [2]],

    ["다음 중 초매개변수로(Hyper Paramemter) 설정이 가능하지 않은 것은? ",  # 78
     [["학습률(Learning Rate)"],
      ["가중치(Weight)"],
      ["은닉층(Hedden Layer)의 수"],
      ["의사결정 나무(Decision Tree)의 깊이"]], [2]],

    ["다음 중 개선 데이터 선정 시 고려 사항으로 가장 알맞지 않은 것은 무엇인가?",  # 79
     [["최신 데이터 적용이나 변수 추가 방식으로 분석 모형을 재조정한다."],
      ["업무 프로세스 KPI의 변경 또는 주요 시스템 원칙 변경, 발생 이벤트의 건수 증가에 따라 성능 평가를 하고 필요하면 재조정한다."],
      ["조건 변화나 가중치 변화 시 계수 값 조정 또는 제약조건 추가로 재조정한다."],
      ["최근 데이터 위주로만 오류율을 점검하고 기존 데이터 집합에 대한 데이터 오류율은 점검하지 않는다."]], [4]],

    ["다음 중 혼동 행렬에 대한 설명으로 적절하지 않은 것은?",  # 80
     [["실제로 부정인 범주 중 부정으로 올바르게 예측(True Negative)한 비율을 정확도(Accuracy)라고 하며, (TP+TN)/(TP+TN+FP+FN)라고 표기한다."],
      ["카파 값(Kappa value)은 0~1 사이의 값을 가지며, 1에 가까울수록 예측값과 실제값이 일치하지 않는 것을 의미한다."],
      ["정밀도(Precision)는 '긍정'으로 예측한 비율 중에서 실제로 긍정인 비율로 TP/(TP+FP)라고 표기한다."],
      ["머신러닝 성능 평가지표 중 오차 비율(Error Rate)을 표기하는 식은 (FP+FN)/(TP+TN+FP+FN)이다."]], [1],1],

    # ["문제",  # 2
    #  [["보기1"],
    #   ["보기2"],
    #   ["보기3"],
    #   ["보기4"]], "정답"],
]

Q_SEQ = random.sample(range(0,len(TOTAL)),len(TOTAL))
for i in range(len(Q_SEQ)):
    print("<"+str(i+1)+"> " + TOTAL[Q_SEQ[i]][0])
    if len(TOTAL[Q_SEQ[i]]) >3 :
        path = 'C:\\Users\\User\\Desktop\\빅분기\\빅데이터Image/'+str(Q_SEQ[i]+1)+'.jpg'
        im = Image.open(path)  # 이미지 불러오기
        im.show()  # 이미지 보여주기
    print()
    ex_rand = random.sample(range(0, 4), 4)
    for j in range(4):
        print(str(j+1)+". "+TOTAL[Q_SEQ[i]][1][ex_rand[j]][0])
    user_answer2=[]
    user_answer = input().split()
    for i2 in range(len(user_answer)):
        user_answer2.append(TOTAL[Q_SEQ[i]][1].index(TOTAL[Q_SEQ[i]][1][ex_rand[int(user_answer[i2])-1]])+1)
    user_answer2 = list(map(int, user_answer2))
    user_answer2.sort()

    if user_answer2 == TOTAL[Q_SEQ[i]][2]:
        count+=1
    else:
        fail.append([Q_SEQ[i]+1,user_answer2])
    print("\n"*100)
    # print(user_answer2, TOTAL[Q_SEQ[i]][2])
print("모든 문제가 끝났습니다.")
print("점수는 " + str(round( (count/len(TOTAL))*100 ,1))+" 점 입니다.")
fail.sort(key=lambda x : (x[0]))
print("틀린문제 " , fail )