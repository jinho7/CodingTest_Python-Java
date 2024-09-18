def solution(targets):
    # 끝점 기준 오름차순 정렬
    targets.sort(key=lambda x: x[1])  
    answer = 0
    #print(targets)
    last_pang = -1
    for start, end in targets:
        if start > last_pang:
            answer += 1
            # 끝점 직전에서 요격
            last_pang = end - 0.1  
            #print("**", last_pang)
    
    return answer