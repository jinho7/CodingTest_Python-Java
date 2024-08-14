def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    current_weight = 0
    
    # 대기 중인 트럭이 있거나 다리 위에 트럭이 있는 동안 반복
    while truck_weights or current_weight > 0:
        time += 1
        # 다리의 맨 앞 요소 제거 & 무게에서 뺌
        current_weight -= bridge.pop(0)
        
        # 대기 중인 트럭이 있음
        if truck_weights:
            # 다음 트럭을 다리에 올릴 수 있는지 확인
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                current_weight += truck
            # 트럭을 올릴 수 없다면 0을 추가 (빈 공간)
            else:
                bridge.append(0)
    
    return time