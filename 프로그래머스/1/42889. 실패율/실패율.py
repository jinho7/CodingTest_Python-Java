def solution(N, stages):
    stages.sort(reverse=True)
    
    # fail에 각 스테이지의 실패한 사람 담아주기
    failed = [0] * N
    for stage in stages:
        if stage != N+1:
            failed[stage-1] += 1
            
    # all_challenger에 각 스테이지 참가자 수
    all_challenger = [0] * N
    for i in range(N):
        sum = 0
        for stage in stages:
            if stage >= i + 1:
                sum += 1
        all_challenger[i] = sum
    
    # rate에 각 스테이지 실패율
    rate = []
    for i in range(N):
        if all_challenger[i] == 0:
            rate.append(0)
        else:
            rate.append(failed[i] / all_challenger[i])
    
    # 순위
    result = sorted(range(1, N+1), key=lambda x: rate[x-1], reverse=True)
    
    return result