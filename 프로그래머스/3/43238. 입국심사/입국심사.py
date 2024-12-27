from itertools import combinations

def solution(n, times):
    # ex1) 40 분이 걸림.
    # 40 / 7 + 40 / 10 => 충분히 6명 처리 가능
    # ex2) 27분이 걸림
    # 27 / 7 + 27 / 10 -> 3명처리, 2명처리 -> 총 5명 밖에 처리 못함.
    
    def check_can_pass(total):
        return sum(total // time for time in times) >= n
    
    left, right = 0, max(times) * n
    print(right)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        # 통과? 일단 answer 해놓고, 더 작은수 가능한지 보기
        if check_can_pass(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer