def can_solve_with_level(diffs, times, limit, level):
    total_time = 0
    n = len(diffs)
    
    for i in range(n):
        diff = diffs[i]
        time_cur = times[i]
        time_prev = times[i - 1] if i > 0 else 0
        
        if diff <= level:
            total_time += time_cur
        else:
            mistakes = diff - level
            # 각 실수당 소요되는 시간
            total_time += (mistakes * (time_cur + time_prev)) + time_cur
            
        # 시간 초과 확인
        if total_time > limit:
            return False
            
    return total_time <= limit

def solution(diffs, times, limit):
    low, high = 1, max(diffs)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if can_solve_with_level(diffs, times, limit, mid):
            answer = mid
            # 더 작은 숙련도를 찾기
            high = mid - 1
        else:
            # 더 큰 숙련도
            low = mid + 1

    return answer
