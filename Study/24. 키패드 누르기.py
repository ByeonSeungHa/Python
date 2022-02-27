def solution(numbers, hand):

    left_hand = [3,0]
    right_hand = [3,2]
    point = []
    numbers = list(map(str, numbers))
    answer = []
    for i in range(len(numbers)):
        if numbers[i] == '1':
            point = [0,0]
        elif numbers[i] == '2':
            point = [0,1]
        elif numbers[i] == '3':
            point = [0,2]
        elif numbers[i] == '4':
            point = [1,0]
        elif numbers[i] == '5':
            point = [1,1]
        elif numbers[i] == '6':
            point = [1,2]
        elif numbers[i] == '7':
            point = [2,0]
        elif numbers[i] == '8':
            point = [2,1]
        elif numbers[i] == '9':
            point = [2,2]
        elif numbers[i] == '':
            point = [3,0]
        elif numbers[i] == '0':
            point = [3,1]
        elif numbers[i] == '#':
            point = [3,2]
        left_dist = abs(left_hand[0]-point[0]) + abs(left_hand[1]-point[1]) # abs는 절대값이다.
        right_dist = abs(right_hand[0]-point[0]) + abs(right_hand[1]-point[1])
        if numbers[i] == '1' or numbers[i] == '4' or numbers[i] == '7':
            answer.append('L')
            left_hand = point
        elif numbers[i] == '3' or numbers[i] == '6' or numbers[i] == '9':
            answer.append('R')
            right_hand = point
        else:
            if left_dist < right_dist:
                answer.append('L')
                left_hand = point
            elif left_dist > right_dist:
                answer.append('R')
                right_hand = point
            elif left_dist == right_dist:
                if hand == "right":
                    answer.append('R')
                    right_hand = point
                elif hand == "left":
                    answer.append('L')
                    left_hand = point
    print(''.join(answer))
    return ''.join(answer)


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
solution(numbers,hand)