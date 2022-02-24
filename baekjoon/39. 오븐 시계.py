A,B = map(int,input().split())
C = int(input())
# 식 순서가 바뀌면 안됀다.
B += C
A += B//60

A%=24
B%=60


print(A,B)

