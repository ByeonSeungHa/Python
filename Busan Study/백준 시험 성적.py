a = int(input())

if a>=90:
    print('A')
elif a>=80:
    print('B')
elif a>=70:
    print('C')
elif a>=60:
    print('D')
else :
    print('F')
#
# def solution (scores): # 만약 학생 성적이 여러개고 등급으로 성적을 나눌 경우
#     jumsoo = [0 for i in range(5)]
#     for x in scores:
#         if 90 <= x <= 100:
#             jumsoo[0] += 1
#         elif 80 <= x <= 89 :
#             jumsoo[1] += 1
#         elif 70 <= x <= 79:
#             jumsoo[2] += 1
#         elif 60 <= x <= 69:
#             jumsoo[3] += 1
#         else:
#             jumsoo[4] += 1
#     print(jumsoo)
#     return jumsoo
#
#
# scores = [86,72,98,60,45]
# solution(scores)