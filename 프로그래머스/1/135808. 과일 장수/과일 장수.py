def solution(k, m, score):
    # 사과 점수 : 1 ~ k
    # 한 상자에서 m개씩 포장 -> 가장 낮은 점수가 p * m -> 상자 가격 (포장하고 남은거 버림)
    # 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익
    score.sort()
    box_num = len(score) // m
    max_benefit = 0
    for i in range(box_num):
        answer = []
        for k in range(m):
            answer.append(score.pop())
        max_benefit += min(answer) * m
    
    return max_benefit