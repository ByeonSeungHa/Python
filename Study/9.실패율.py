def solution(N, stages):
    dic = {}
    list_1 = []
    for i in range(len(stages)): # dic에 stages를 담는다.
        if stages[i] not in dic: # dic은 stages에서 떨어진 사람수이다.
            dic[stages[i]]=1
        else:
            dic[stages[i]]+=1
    print(dic) # {key : value} = {stages : 떨어진사람수}
    boonmo=0
    boonja=0
    for i in range(1,N+1):
        for j in dic:
            if i<= j :
                boonmo+= dic.get(j) # dic.get(j)  ->  j 스테이지에서 떨어진 사람수
        boonja = dic.get(i)
# dic.get(i)   -> 그 스테이지에 있는 사람 수
# 3
# +1
# +1
# +2
# boonmo = 7
# boonja = 3
# dic.get(i)
        if boonja is None:
            boonja=0
        if boonmo==0:
            list_1.append([i,0])
        else:
            list_1.append([i,boonja/boonmo])
        boonmo=0
    answer = []
    list_1.sort(key=lambda x : (-x[1], x[0])) # x[0]는 i기준 오름차순 -x[0]는 내림차순
    for i in range(len(list_1)):              # x[1]는 boonja/boonmo기준으로 오름차순 내림차순
        answer.append(list_1[i][0])           # 이중리스트 에서 원소개수가 같은땐 람다식이 편하다.


    return answer