def solution(board, moves):
    answer = 0
    board2 = list(map(list, zip(*board)))
    baguni = []
    for i in range(len(moves)):
        num_1 = board2[moves[i]-1]
        for j in range(len(num_1)):
            if num_1[j] != 0:
                baguni.append(num_1[j])
                num_1[j] = 0
                for k in range(len(baguni)-1):
                    if baguni[k] == baguni[k+1]:
                        baguni.pop(k)
                        baguni.pop(k)
                        answer += 2
                        break
                break

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board,moves)
