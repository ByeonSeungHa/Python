n, m = map(int, input().strip().split(' '))
for i in range(m):
    word = ""
    for j in range(n):
        word += "*"
    print(word)