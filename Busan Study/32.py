def solution(arr, k):
    arr_list = []
    for i in arr:
        for j in i:
            arr_list.append(j)
    n = sorted(arr_list)
    s = n[k-1]
    return s