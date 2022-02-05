def solution(a, b):
    cal = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = 0
    days = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    for i in range(a-1):
        day += cal[i]
    day += b
    print(days[day%7] )
    print(day)
    return (days[day%7] )