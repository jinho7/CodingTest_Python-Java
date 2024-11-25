def solution(routes):
    # 끝 점부터 정렬하는 이유
    # 앞에서부터 체크 했을 때, "현재보다 앞에서 끝나는 구간은 더 이상 없다"는 게 보장
    routes.sort(key = lambda x:x[1])
    print(routes)
    temp = -30001
    answer = 0
    for route in routes:
        start, end = route
        # 끝점으로 카메라 새로 놓기
        if start > temp :
            temp = end
            answer += 1
        # 나머지는 괜찮
            
    return answer