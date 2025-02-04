import math

def solution(n, stations, w):
    answer = 0
    unreachable = []
    
    # 첫 기지국까지의 처리
    if stations[0]-w > 1:
        unreachable.extend([1, stations[0]-w-1])
    
    #  기지국 간 간격 처리
    for i in range(len(stations)-1):
        if stations[i]+w+1 < stations[i+1]-w:
            unreachable.extend([stations[i]+w+1, stations[i+1]-w-1])
            
    # 마지막 기지국 이후 처리
    if stations[-1]+w < n:
         unreachable.extend([stations[-1]+w+1, n])
                
    # 간격마다 필요한 기지국 수 계산
    for j in range(0, len(unreachable), 2):
        answer += math.ceil((unreachable[j+1] + 1 - unreachable[j]) / (2*w+1))
        
    return answer