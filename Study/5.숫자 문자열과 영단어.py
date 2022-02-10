def solution(s):
    suzza = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # 숫자도 문자로 인식
    moonza = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    list_1 = []
    word = ""
    for i in range(len(s)):
        if s[i] in suzza:
            list_1.append(s[i])
        else:
            word += s[i]
            if word in moonza:
                list_1.append(suzza[moonza.index(word)])
                word="" # 초기화를 시켜주어야한다. 안그럼 문자를 숫자로 바꿨을 때 붙어있다.
    print(list_1)
    return int(''.join(list_1))