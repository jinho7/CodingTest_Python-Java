def solution(N, stages):
    # 각 스테이지에 도달한 플레이어 수 계산
    reach = [0] * (N + 2)
    for stage in stages:
        reach[stage] += 1
    
    # 각 스테이지의 도전자 수 계산
    total = len(stages)
    challengers = [total] * (N + 1)
    for i in range(1, N + 1):
        challengers[i] = challengers[i-1] - reach[i-1]
    
    # 실패율 계산 및 정렬
    failure_rates = []
    for i in range(1, N + 1):
        if challengers[i] == 0:
            rate = 0
        else:
            rate = reach[i] / challengers[i]
        failure_rates.append((-rate, i))
    
    # 정렬 후 스테이지 번호만 반환
    failure_rates.sort()
    return [stage for _, stage in failure_rates]



def my_solution(N, stages):
    
    stages.sort(reverse=True)
    
    failed = []
    for i in range(N):
        failed.append(0)
        
    for i in range(len(stages)):
        if stages[i] != N+1:
            failed[stages[i]-1] += 1
            
    for i in range(len(stages)):
        if stages[i] != N+1:
            failed[stages[i]-1] /= all_challenger(stages, i+1)
            
    return failed

# k 스테이즈의 총 참가자 수
def all_challenger(stages, k):
    sum = 0
    for i in range(len(stages)):
            if stages[i] >= k:
                sum += 1
    return sum