def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries_stack = []
    pickups_stack = []

    # 스택 초기화
    for i in range(n):
        if deliveries[i] > 0:
            deliveries_stack.append((i, deliveries[i]))
        if pickups[i] > 0:
            pickups_stack.append((i, pickups[i]))
            

    while deliveries_stack or pickups_stack:
        # 가장 먼 거리 계산
        max_index = max(deliveries_stack[-1][0] if deliveries_stack else 0,
                        pickups_stack[-1][0] if pickups_stack else 0)
        
        answer += 2 * (max_index + 1)  # 왕복 거리 추가
        
        # 배달 처리
        go_cap = cap
        while deliveries_stack and go_cap > 0:
            i, amount = deliveries_stack.pop()
            if amount <= go_cap:
                go_cap -= amount
            else:
                deliveries_stack.append((i, amount - go_cap))
                break
        
        # 수거 처리
        come_cap = cap
        while pickups_stack and come_cap > 0:
            i, amount = pickups_stack.pop()
            if amount <= come_cap:
                come_cap -= amount
            else:
                pickups_stack.append((i, amount - come_cap))
                break

    return answer