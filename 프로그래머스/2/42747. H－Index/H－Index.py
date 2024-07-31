def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순으로 정렬
    h_index = 0
    
    for index, citation in enumerate(citations):
        if index + 1 <= citation :  # 현재 논문의 인용 횟수가 (i+1)편 이상인 경우
            h_index = index + 1
        else:
            break  # 더 이상 h-index를 증가시킬 수 없으므로 반복 중단
    
    return h_index