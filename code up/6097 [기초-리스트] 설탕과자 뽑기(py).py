# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
# ------

# 부모님과 함께 놀러간 영일이는
# 설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

# 길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

# 막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
# (잉어, 붕어, 용 등 여러 가지가 적혀있다.)

# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

h,w = input().split()
h = int(h)
w = int(w)
m = []
for i in range(h+1) :
    m.append([])
    for j in range(w+1) :
        m[i].append(0)
n = int(input())
for i in range(n) :
    l,d,x,y = input().split()
    if int(d)==0 :
        for j in range(int(l)) :
            m[int(x)][int(y)+j] = 1
    else :
        for j in range(int(l)) :
            m[int(x)+j][int(y)] = 1
for i in range(1, h+1) :
    for j in range(1, w+1) :
        print(m[i][j], end=' ')
    print()


# h, w = map(int, input().split())
# n = int(input())
# zeros = [[0] * w for _ in range(h)]
# for i in range(n):
#     l, d, x, y = map(int, input().split())
#     for j in range(l):
#         if d == 0:
#             zeros[x-1][y-1+j] = 1
#         else:
#             zeros[x-1+j][y-1] = 1
# for i in range(h):
#     for j in range(w):
#         print(zeros[i][j], end=' ')
#     print(end='\n')

# 먼저 h, w, n을 각각 입력받습니다. 그리고 zeros라는 2차원 배열을 만들어줍니다.
# zeros는 가로로 w, 세로로 h 크기의 0으로 이루어진 배열입니다.
# zeros 배열을 만들 때 '리스트 컴프리헨션' 문법을 사용하였습니다. 이는 이차원 배열을 생성할 때 효율적입니다.
# 그 다음 for 반복문으로 n번 l, d, x, y를 입력받습니다.
# 이제 입력값들을 토대로 zeros 배열을 1로 할당해야 합니다. 각 막대의 l, d, x, y 속성을 이용하여 할당해주겠습니다.
# for 반복문으로 막대의 l 입력값만큼 반복해주고, if 조건문으로 d가 0일 때는 가로, 1일 때는 세로로 조건을 걸어줍니다.
# d가 0일 때 (가로일 때)는 [x-1][y-1+j] 만큼의 위치를 1로 변환합니다.
# d가 1일 때 (세로일 때)는 [x-1+j][y-1] 만큼의 위치를 1로 변환합니다.
# 각각 x, y에서 1씩 빼주는 이유는 입력 좌표 x, y가 0,0부터 시작하는 것이 아닌 1,1부터 시작하기 때문입니다.
# 전부 할당하였으면 zeros 리스트에 저장된 값들을 for 반복문으로 출력해주어야 합니다.
# print() 함수의 end 옵션을 사용하여서 문제에서 제시한 출력 예시와 같이 출력해줍니다.