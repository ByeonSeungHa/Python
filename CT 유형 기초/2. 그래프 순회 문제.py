고양이 찾기 (그래프 순회 문제)

알잡이는 자신이 좋아하는 고양이가 어떤경로로 이동하는지 알게되었다
고양이는 한 시간에 한번 이동하고, 알잡이의 예상대로 움직인다고 할 때 m시간 뒤에 고양이가 있는 위치를 구하여라
고양이의 시작위치는 무조건 1번이다.

이동 방법은 다음과 같은 형식으로 주어진다.

2 4 1 5 3
1 -> 2
2 -> 4
4 -> 5
5 -> 3
3 -> 1 이다.


2 4 1 5 3,  8(번 움직여라)
1-2-4-5-3-1-2-4-5
답은 5 가된다.

문제
1번) 2 4 5 4 3, 12
1->2
2->4
3->5
4->4
5->3
1->2->4->4
0   1   2   3
12%2

답은 4

2번) 5 4 2 2 4, 60
1->5
2->4
3->2
4->2
5->4
1->5->4->2->4->2
         0   1
60%2

답은 4

3번) 3 1 4 2 4, 120
1->3
2->1
3->4
4->2
5->4
1->3->4->2->1
0   1   2   3
120%4

답 1

4번) 6 5 9 5 3 4 8 5 1, 600
1->6
2->5
3->9
4->5
5->3
6->4
7->8
8->5
9->1
열결 되는걸 뽑으면 (무조건 1시작)
1->6->4->5->3->9->1 (반복)
0   1   2   3   4   5 총 6개 600%6하면 0이다 답은 1이다.

답 1

5번) 2 4 6 8 10 1 3 5 7 9, 1150
1->2
2->4
3->6
4->8
5->10
6->1
7->3
8->5
9->7
10->9
1->2->4->8->5->10->9->7->3->6->1
0   1   2   3   4    5    6   7   8   9
1150%10

답1
