def solution(weights):
    answer = 0
    dic = { weight : 0 for weight in weights}
    weights.sort()
    
    for weight in weights:
        if dic[weight]:
            answer += dic[weight]
            
        dic[weight] += 1
            
        if weight % 2 == 0:
            try:
                dic[(weight//2) * 3] += 1
            except KeyError:
                dic[(weight//2) * 3] = 1   
                
        if weight % 3 == 0:
            try:
                dic[(weight//3) * 4] += 1
            except KeyError:
                dic[(weight//3) * 4] = 1   
        
        try:
            dic[weight * 2] += 1
        except KeyError:
            dic[weight * 2] = 1   
            
    return answer