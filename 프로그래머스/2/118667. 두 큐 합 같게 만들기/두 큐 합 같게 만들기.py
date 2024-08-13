# 아이디어
# 실제 큐에서 insert / pop 안하고
# 포인터와 합 변수만을 사용
# 그리고 한 쪽 큐에서만 전체합/2 되면 끝
# 왼쪽 꺼만 생각
# 이동 시 포인터를 두 개 두고, 합친 큐를 하나로 생각
# | 3, 2, 7, 2, | 4, 6, 5, 1
# max는 3, 2, 7, 2, 4, 6, 5, 1 || 이 상황
def solution(queue1, queue2):
    # 전체 큐의 합과 목표값 계산
    total = sum(queue1) + sum(queue2)
    target = total // 2
    
    # 홀수면 불가능
    if total % 2 != 0:
        return -1
    
    # 두 큐를 하나의 리스트로 연결
    queue = queue1 + queue2
    n = len(queue1)
    
    # 포인터와 합 변수 초기화
    left, right = 0, n - 1
    current_sum = sum(queue1)
    count = 0
    
    while count < n * 3:  # 최대 이동 횟수 제한
        if current_sum == target:
            return count
        
        if current_sum < target:
            right = (right + 1) % (2 * n)
            current_sum += queue[right]
            count += 1
        else:
            current_sum -= queue[left]
            left = (left + 1) % (2 * n)
            count += 1
    
    return -1  # 목표에 도달하지 못함