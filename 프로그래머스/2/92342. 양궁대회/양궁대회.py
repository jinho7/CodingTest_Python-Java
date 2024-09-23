from itertools import combinations

def solution(n, info):
    def calculate_score(ryan):
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            if ryan[i] > info[i]:
                ryan_score += 10 - i
            elif info[i] > 0:
                apeach_score += 10 - i
        return ryan_score - apeach_score

    max_score = 0
    answer = []

    # 1부터 11까지의 과녁 개수
    for i in range(1, 12):  
        for combo in combinations(range(11), i):
            ryan = [0] * 11
            left = n
            for idx in combo:
                if left > info[idx]:
                    ryan[idx] = info[idx] + 1
                    left -= ryan[idx]
                if left <= 0:
                    break
            if left > 0:
                ryan[10] += left  # 남은 화살은 모두 0점에 쏘기

            score = calculate_score(ryan)
            if score > max_score:
                max_score = score
                answer = ryan
            elif score == max_score and ryan[::-1] > answer[::-1]:
                answer = ryan

    return answer if max_score > 0 else [-1]