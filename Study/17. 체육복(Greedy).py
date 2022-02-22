def solution(n, lost, reserve):
    set_reserve = list(set(reserve)-set(lost)) # 여벌 체육복이 있는 학생이 도난당한 경우의 수 삭제
    set_lost = list(set(lost)-set(reserve))    # 여벌 체육복이 있는 학생이 도난당한 경우의 수 삭제
    # 앞의 식을 넣지않으면 도난당했지만 여벌 체육복을 남한테 빌려주는 상황이 생긴다.
    # 앞의 식은 도난당한 체육복을 여벌체육복을 스스로 처리하는 식이다.
    for i in range(len(set_reserve)): # remove는 빼주는 기능
        if set_reserve[i] - 1 in set_lost:
            set_lost.remove(set_reserve[i]-1)
        elif set_reserve[i] + 1 in set_lost:
            set_lost.remove(set_reserve[i]+1)
    answer = n - len(set_lost)
    return answer