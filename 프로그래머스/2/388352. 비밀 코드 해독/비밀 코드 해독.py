from itertools import combinations

def solution(n, q, ans):
    
    # 다 검색해보자. (Brute Force)
    candidates = list(combinations([i for i in range(1, n+1)], 5))
    # 그나마 효율을 챙기려면? ans이 가장 높은거 부터 체크!
    sorted_ans, sorted_q = zip(*sorted(zip(ans, q), key=lambda x: x[0], reverse=True))

    answer = 0
    for candidate in candidates:
        condition = True
        for i in range(len(sorted_q)):
            # sorted_q[i] 안에서 sorted_ans[i]개 맞아야 됨.
            if len(set(candidate) & set(sorted_q[i])) != sorted_ans[i]:
                condition = False
                break
        if condition:
            answer += 1
        
    return answer
