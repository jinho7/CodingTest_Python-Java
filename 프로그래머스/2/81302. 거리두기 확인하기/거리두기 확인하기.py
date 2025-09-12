def solution(places):
    
    def calculate_manhattan_distance(x1, y1, x2, y2):
        return abs(x2-x1) + abs(y2-y1)
    
    def check_rule(place):
        # 1. 각 응시자 위치 저장
        p_location = []
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P' :
                    p_location.append((i, j))
    
        # 2. 일대일로 체크
        for i in range(len(p_location)-1):
            for j in range(i+1, len(p_location)):
                x1, y1 = p_location[i]
                x2, y2 = p_location[j]
                dist = calculate_manhattan_distance(x1, y1, x2, y2)

                # 2-1. 맨하튼 거리 1 있을 경우 바로 return 0
                if dist < 2:
                    return 0
                # 2-2. 맨하튼 거리 2 있을 경우 추가 체크
                elif dist == 2:
                    # (1자 사이), (ㄱ자 사이) 2가지로 추가 검증
                    # 2-2-1. 1자: x축 or y축
                    if x1 == x2:
                        if place[x1][(y1+y2)//2] != 'X':
                            return 0
                    elif y1 == y2:
                        if place[(x1+x2)//2][y1] != 'X':
                            return 0
                    # 2-2-2. ㄱ자
                    else:
                        if place[x1][y2] != 'X' or place[x2][y1] != 'X':
                            return 0
                # 2-3. 맨하튼 거리 2 초과 모두 continue
                else:
                    continue
        # 3. 모두 통과 시 return 1
        return 1

    answer = []
    for i in range(len(places)):
        answer.append(check_rule(places[i]))
    return answer