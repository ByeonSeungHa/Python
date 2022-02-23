def solution(answers):
    supoja1 = [1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer1 = 0
    answer2 = 0
    answer3 = 0
    answer = []
    answer_2 = []
    for i in range(len(answers)):
        if answers[i] == supoja1[i % 5]:
            answer1 += 1
        if answers[i] == supoja2[i % 8]:
            answer2 += 1
        if answers[i] == supoja3[i % 10]:
            answer3 += 1
    answer.append([1, answer1])
    answer.append([2, answer2])
    answer.append([3, answer3])  # 번호랑 점수를 리스트로 넣음
    answer.sort(key=lambda x: (-x[1], x[0]))  # 점수로 내림차순 점수같으면 번호로 오름차순
    # lambda식은 2중 리스트일 때 원하는 순서로 정렬할 때 사용한다.

    # answer 에는 번호랑 점수리스트가 정렬 되서 들어와있음

    # 1등은 무조건 1명은 있음.

    answer_2.append(answer[0][0])  # 1등의 번호를 넣어줌 [1,5][2,0][3,0] 이면 [1,5]를 나타낸것이다.
    for i in range(1, len(answer)):  # for 문을 돌려서
        if answer[0][1] == answer[i][1]:  # 1등의 점수랑 i번째 사람의 점수가 같으면 답에 넣어준다.
            answer_2.append(answer[i][0])

    return answer_2