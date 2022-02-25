a, b, c = map(int, input().split())

if a == b == c: # 3개 숫자가 다 같을 때
    print(10000+a*1000)
elif a == b: # 2개 숫자가 같을 때때
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else: # 모든 숫자가 다를 때
    print(100 * max(a,b,c))