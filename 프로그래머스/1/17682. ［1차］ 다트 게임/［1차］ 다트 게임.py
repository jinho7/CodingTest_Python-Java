def solution(dartResult):
    scores = []
    current_score = ''
    
    for i in dartResult:
        if i.isdigit():
            # 숫자 두번 연속나오면 더해짐 (10고려)
            current_score += i
        elif i in ['S', 'D', 'T']:
            score = int(current_score)
            if i == 'D':
                score **= 2
            elif i == 'T':
                score **= 3
            scores.append(score)
            current_score = ''
        elif i in ['*', '#']:
            if i == '*':
                scores[-1] *= 2
                if len(scores) > 1:
                    scores[-2] *= 2
            else:  # '#'
                scores[-1] *= -1
    
    return sum(scores)