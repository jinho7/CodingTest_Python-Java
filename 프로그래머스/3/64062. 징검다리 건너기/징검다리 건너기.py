def solution(stones, k):

    def check_go(n):
        count = 0  # 연속된 못 건너는 돌의 개수
        
        for stone in stones:
            if stone < n:  # 현재 돌을 못 건너는 경우
                count += 1
            else:  # 현재 돌을 건널 수 있는 경우
                count = 0
                
            if count >= k:  # 연속된 k개의 돌을 건널 수 없음
                return False
        return True
    
    
    # 인덱스
    left, right = 0, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        # 통과 가능
        if check_go(mid):
            left = mid + 1
        # 통과 불가능
        else:
            right = mid -1

    return right
