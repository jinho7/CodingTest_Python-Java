def solution(elements):
    # 일단 mod를 써야겠다.
    # 그냥 두배로 늘려..
    sum_set = set()
    element = elements + elements
    length = len(elements)
    
    for i in range(1, length+1):
        #print("i", i)
        for k in range(0, length):
            #print("k", k, "k+i", k+i)
            sum_set.add(sum(element[k: k+i]))
    return len(sum_set)