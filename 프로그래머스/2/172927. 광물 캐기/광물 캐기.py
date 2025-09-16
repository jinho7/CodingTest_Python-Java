def solution(picks, minerals):
    
    answer = 0
    
    types = ['diamond', 'iron', 'stone']
    cost = {i: j for i, j in zip(types, [
        {x: y for x, y in zip(types, [1, 1, 1])},
        {x: y for x, y in zip(types, [5, 1, 1])},
        {x: y for x, y in zip(types, [25, 5, 1])}
    ])}

    # 5개 씩 쪼갠 뒤, 각 그룹을 뭘로 캐는게 좋을지 묻는 것!
    group_weight = []
    
    # 1. 그룹화 (가중치 3, 2, 1 순) - 그냥 stone꺼 쓰면 되네.
    for i in range(0, len(minerals), 5):
        weight = 0
        for j in minerals[i:i+5]:
            weight += cost['stone'][j]
        group_weight.append((weight, minerals[i:i+5]))
    
    
    # 곡괭이 수 < 그룹 수 더 많으면, 앞에서부터 곡갱이 수만큼 짤라야함.
    # 아니면, 앞쪽 안 캐고 뒤에만 경우가 생김. (순서대로 캐야함)
    
    if sum(picks) < len(group_weight):
        group_weight = group_weight[0:sum(picks)]
        
    
    # 2. 그룹별 가중치를 내림차순으로 정렬
    group_weight.sort(reverse=True)
    print(group_weight)
    
    # 3. 다이아 - 철 - 돌 순으로 곡괭이 사용
    
    # picks를 다 쓰면 끝.
    # 광물 수가 더 많은 경우는 위에서 잘랐음
    for i in range(len(group_weight)):
        if sum(picks) == 0:
            break
        pick_type = ''
        # 곡괭이 선택
        for j in range(3):
            if picks[j] > 0:
                picks[j] -= 1
                pick_type = types[j]
                break
        
        # 그룹 실제로 캐기
        for mineral in group_weight[i][1]:
            answer += cost[pick_type][mineral]
        i += 1
    
    return answer