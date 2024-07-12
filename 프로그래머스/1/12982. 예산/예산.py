def solution(d, budget):
    d.sort()
    
    sum = 0
    count = 0

    for cost in d:
        if sum + cost > budget:
            break
        sum += cost
        count += 1
        
    return count