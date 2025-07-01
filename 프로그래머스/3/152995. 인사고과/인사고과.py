def solution(scores):
    # 근무 태도 점수 a / 동료 평가 점수 b
    # 타 임원보다 두 점수가 모두 낮은 경우 1번이라도 있으면 : 인센티브 제외
    # (a[i] < a[j] and b[i] < b[j]) - a는 sort 해놓음
    # else : 두 점수 합 높은 순 <- 인센티브 차등 지급
        # 동석차의 수 만큼 다음 석차 건너 뛰기 (공동 석차)
    
    index_scores = [[x[0], x[1], i] for i, x in enumerate(scores)]
    # a는 내림차순, b는 오름차순
    index_scores.sort(reverse = True, key = lambda x: (x[0], -x[1]))
    
    max_b = -1
    insentive = []
    for i in range(len(index_scores)):
        if index_scores[i][1] >= max_b:
            max_b = index_scores[i][1]
            insentive.append(index_scores[i])
        else:
            if index_scores[i][2] == 0:
                return -1
    
    insentive.sort(reverse = True, key = lambda x: (x[0] + x[1]))
    
    rank = 0
    same_rank = 0
    sum_scores = -1
    for a, b, idx in insentive:
        if sum_scores == (a + b):
            same_rank += 1
        else:
            if same_rank == 0:
                rank += 1
            else:
                rank += 1
                rank += same_rank
                same_rank = 0
            sum_scores = (a + b)
        if idx == 0:
            return rank