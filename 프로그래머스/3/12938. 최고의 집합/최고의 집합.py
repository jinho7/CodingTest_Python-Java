def solution(n, s):
    # 원소 개수 n
    # 합 s
    
    # 최대한 고르게
    base = s // n
    remain = s % n
    
    if base == 0:
        return [-1]
    answer = [base for _ in range(n-remain)]
    answer.extend([(base+1) for _ in range(remain)])
    return answer