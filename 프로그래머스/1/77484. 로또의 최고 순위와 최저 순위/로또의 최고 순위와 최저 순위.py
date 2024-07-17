def solution(lottos, win_nums):
    
    zero = lottos.count(0)
    correct = 0
    # 역순으로 순회
    for a in range(len(lottos)):
        if lottos[a] in win_nums:
            correct += 1
            
    max_ = correct + zero
    min_ = correct
    max_rank = 7- max_ if max_ >=1 else 6
    min_rank = 7- min_ if min_ >=1 else 6
    return [max_rank, min_rank]