def njinbub(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n):
    s = njinbub(n, 3)
    s = list(s)
    s.reverse()
    s2 = ''.join(s)
    print(int(s2, 3))

    return int(s2, 3)