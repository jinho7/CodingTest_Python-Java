def solution(storey):
    answer = 0
    
    while storey > 0:
        i = storey % 10
        storey = storey // 10

        # 올림
        if i > 5 or (i == 5 and storey % 10 >= 5):
            storey += 1
            answer += (10-i)
        # 내림
        else:
            answer += i
    return answer