def solution(weights: list):
    answer = 0
    
    dict = {}

    for i in weights:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            
    for i in dict:
        # 같은 무게가 두 개 이상 있을 경우
        if dict[i] >= 2:
            num = dict[i]
            answer += (num * (num-1)) //2
            
        for m in [2, 2/3, 3/4]:
            if i*m in dict:
                answer += dict[i] * dict[i*m]
        
    return answer