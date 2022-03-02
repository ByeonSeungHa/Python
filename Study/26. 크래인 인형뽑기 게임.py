def solution(board, moves):
    answer = 0
    board2 = list(map(list, zip(*board)))  # 가로배열을 세로로바꾼다.
    stack = []
    for i in range(len(moves)):
        temp = moves[i] - 1
        for j in range(len(board2[temp])):
            if board2[temp][j] != 0:
                stack.append(board2[temp][j])
                board2[temp][j] = 0
                if len(stack) >= 2:
                    if stack[-2] == stack[-1]:
                        stack.pop()
                        stack.pop()
                        answer += 2

                break

    return answer

# 고양이1 토끼2 개5 피치4 오리3