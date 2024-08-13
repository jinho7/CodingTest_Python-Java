def solution(queue1, queue2):
    arr = queue1 + queue2
    total_sum = sum(arr)
    target = total_sum // 2
    
    if total_sum % 2 != 0:
        return -1  # 홀수인 경우 불가능
    
    queue1_sum = sum(queue1)
    queue2_sum = total_sum - queue1_sum
    max_operations = len(arr) * 2  # 최대 작업 횟수 설정
    answer = 0
    
    p1, p2 = 0, 0  # 각 큐의 시작 포인터
    
    while answer <= max_operations:
        if queue1_sum == target:
            return answer
        
        if queue1_sum > target:
            if p1 >= len(queue1):
                return -1
            val = queue1[p1]
            queue1_sum -= val
            queue2_sum += val
            queue2.append(val)
            p1 += 1
        else:
            if p2 >= len(queue2):
                return -1
            val = queue2[p2]
            queue2_sum -= val
            queue1_sum += val
            queue1.append(val)
            p2 += 1
        
        answer += 1
    
    return -1  # 합이 같아지는 지점을 찾지 못함