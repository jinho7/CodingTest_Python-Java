import math

def solution(progress, speeds):
    answer = []
    days = []
    count = 1

    for i in range(len(progress)):
        x = (100 - progress[i]) / speeds[i]
        days.append(math.ceil(x))
        
    # 배포 가능한 기능 개수 계산
    max_days = days[0]  # 첫 작업의 소요 일수
    count = 1          # 현재 배포할 기능 개수
    
    for i in range(1, len(days)):
        if days[i] <= max_days:  # 현재 작업이 이전 작업보다 일찍 또는 동시에 끝나는 경우
            count += 1
        else:  # 현재 작업이 이전 작업보다 더 오래 걸리는 경우
            answer.append(count)
            max_days = days[i]
            count = 1
    
    answer.append(count)  # 마지막 배포 추가
    return answer