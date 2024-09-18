def solution(cards):
    # 각 카드 번호를 인덱스로 변환 (0부터 시작)
    index_cards = [index - 1 for index in cards]
    group_sizes = []
    
    # 상자의 방문 여부를 체크하는 리스트
    visited = [False for _ in index_cards]
    
    # 각 상자의 그룹을 찾는 과정
    for i in range(len(index_cards)):
        if not visited[i]:
            group_size = 0
            current = i
            
            # 방문했던 상자로 되돌아오면 stop
            while not visited[current]:
                visited[current] = True
                group_size += 1
                # 다음 상자(= 인덱스 i인 상자) 로 이동
                current = index_cards[current]
            
            group_sizes.append(group_size)
    
    # 그룹이 2개 이상일 때만 점수를 계산
    if len(group_sizes) < 2:
        return 0
    
    group_sizes.sort(reverse=True)
    
    return group_sizes[0] * group_sizes[1]
