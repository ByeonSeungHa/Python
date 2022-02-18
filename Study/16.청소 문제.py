# 3. NXN 크기의 2차원 배열 격자형태, 물건이 놓인 칸은 -1, 쌓여있는 먼지의 양은 0 이상의 정수
# 로봇청소기로 쌓여있는 먼지 청소,
# go 현재 바라보는 방향 한칸 전진
# left 왼쪽으로 회전
# right 오른쪽으로 회전
# 로봇청소기가 방문한 칸은 먼지의 양이 0이 됨
# 현재 사무실의 상태를 나타내는 2차원 배열 office
# 로봇청소기가 놓여있는 칸의 좌표 r, c,
# 로봇청소기가 처리하는 명령어가 들어있는 배열 move
# 로봇청소기가 주어진 명령어를 모두 처리 후 청소한 먼지의 양을 return하는 함수 완성
# 단 로봇청소기는 처음에 항상 북쪽을 바라본 상태로 시작한다고 가정
#
# -1은 물건이 놓여있어 지나갈 수 없는 칸
# r은 북-남 방향의 좌표
# c는 서-동 방향의 좌표
# 로봇청소기는 처음에 항상 0이상의 정수가 적혀있는 칸에만 놓여있음
# move 배열에는 go, left, right단어만 들어있음
#
# office			r	c	move					result
# [[5,-1,4], [6,3,-1],[2,-1,1]]	1	0	["go","go","right","go","right","go","left","go"] 	14
#
# 5  -1  4
# 6  3  -1
# 2  -1  1

from collections import deque

def solution(office, r, c, move):
    global table
    table = [[0 for _ in range(len(office[0]))] for _  in range(len(office))]  #크기 9999의 board 초기화
    direction = 4 # 동서남북 4방향이라서 4이다 그중 북에서 시작한다.

    table[r][c]=office[r][c]= 0  # 출발지를 0으로 초기화
    office[r][c] = 0

    for i in range(len(move)):
        if direction == 1 and move[1] == "left":
            direction = 4
        elif direction == 1 and move[1] == "right":
            direction = 3
        elif direction == 2 and move[1] == "left":
            direction = 3
        elif direction == 1 and move[1] == "right":
            direction = 3
        elif direction == 1 and move[1] == "left":
            direction = 3
        elif direction == 1 and move[1] == "right":
            direction = 3
        elif direction == 1 and move[1] == "left":
            direction = 3
        elif direction == 4 and move[1] == "right":
            direction = 2
        elif direction == 4 and move[1] == "left":
            direction = 1
        elif move[i] == "go":
            go(direction, office, table,r,c)
    return 0

def go(direction, office, table,r,c):
    dx = [-1, 1, 0, 0]   #
    dy = [0, 0, -1, 1]   #상하좌우를 담아줌
    x= c
    y= r       #x,y  좌표 담아줌

    n= len(office)      # 좌표크기
    m= len(office[0])   # 좌표크기

    if direction ==1:
        nx = x + dx[1]  # 0일 때 왼쪽으로, 1일 때 오른쪽, 2일 때 아래로 한 칸, 3일 때 위로 한 칸
        ny = y + dy[1]
        if nx >= n or ny >= m or nx < 0 or ny < 0:  # 좌표 범위를 넘어가면 무시때림
            return
        if office[nx][ny] == 1:
            return
        else:
            table[nx][ny] = table[x][y] + office[nx][ny]
            print(table)
            r = ny
            c = nx
            office[nx][ny] = 0
    return 0  #end 좌표를 table에서 찾은 값


office = [[5,-1,4], [6,3,-1],[2,-1,1]]  # map
table = []
r = 1 #좌표
c = 0
# 보드
move = ["go","go","right","go","right","go","left","go"]
# 자원을 부수는 데 드는 비용
solution(office, r, c)