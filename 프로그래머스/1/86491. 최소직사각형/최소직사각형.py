def solution(sizes):
    first_max = 0
    second_max = 0
    
    for item in sizes:
        if (item[0] < item[1]):
            temp = item[0]
            item[0] = item[1]
            item[1] = temp
            
    for item in sizes:
        if item[0] > first_max:
            first_max = item[0]
        if item[1] > second_max:
            second_max = item[1]
    return first_max * second_max