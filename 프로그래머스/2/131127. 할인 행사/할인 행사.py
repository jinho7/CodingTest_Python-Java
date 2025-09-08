from collections import defaultdict

def solution(want, number, discount):
    want_amount = defaultdict(int)
    for x, y in zip(want, number):
        want_amount[x] = y
    
    answer = 0
    for i in range(len(discount) - 9):
        count_dict = want_amount.copy()
        
        # validate
        for x in discount[i:i+10]:
            if count_dict[x] != 0:
                count_dict[x] -= 1
        if sum(count_dict.values()) == 0:
            answer += 1
    return answer