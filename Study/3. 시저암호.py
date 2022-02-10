def solution(s, n): # 시저 암호는 s를 n만큼 돌린 암호이다.
    alpha_list = []  # 알파벳 a를 1만큼 돌리면 b이다.
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122: # 알파벳 소문자는 97~122이다.
            k = ord(s[i]) + n
            while True:
                if 97 <= k <= 122:
                    break
                else:
                    k -= 26 # 알파벳의 개수는 26개이다.
            alpha_list.append(chr(k))
        elif 65 <= ord(s[i]) <= 90: # 알파벳 대문자는 65~90이다.
            k = ord(s[i]) + n
            while True:
                if 65 <= k <= 90:
                    break
                else:
                    k -= 26
            alpha_list.append(chr(k))
        else:
            alpha_list.append(s[i])

    return ''.join(alpha_list)