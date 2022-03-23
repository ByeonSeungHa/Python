#You may use import as below.
#import math

def solution(shirt_size):
    answer = []
    shirt_list = [0 for _ in range(6)]
    for i in shirt_size:
        if i == "XS":
            shirt_list[0] += 1
        elif i == "S":
            shirt_list[1] += 1
        elif i == "M":
            shirt_list[2] += 1
        elif i == "L":
            shirt_list[3] += 1
        elif i == "XL":
            shirt_list[4] += 1
        elif i == "XXL":
            shirt_list[5] += 1
    return shirt_list

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")