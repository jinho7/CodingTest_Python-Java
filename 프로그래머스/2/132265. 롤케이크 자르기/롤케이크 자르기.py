def solution(topping):
    sum = 0
    left = set()
    right = {}
    
    # 각 요소의 빈도를 미리 계산
    for t in topping:
        if t in right:
            right[t] += 1
        else:
            right[t] = 1
    
    for i in range(len(topping)):
        # 왼쪽 파트에 요소 추가
        if topping[i] not in left:
            left.add(topping[i])
            
        if topping[i] in right:
            if right[topping[i]] == 1:
                del right[topping[i]]
            else:
                right[topping[i]] -= 1
                
        if len(left) == len(right):
            sum += 1
    return sum