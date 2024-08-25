from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    result = []
    
    for c in course:
        freq_dict = defaultdict(int)
        for order in orders:
            # 오름차순 안하면, XY, YX 다르게 집계됨
            for comb in combinations(sorted(list(order)), c):
                a = ''.join(comb)
                freq_dict[a] += 1
                
        # freq_dict 있다면,
        if freq_dict:
            max_value = max(freq_dict.values())
            if max_value >= 2:
                for key, value in freq_dict.items():
                    if value == max_value:
                        print(value)
                        result.append(key)
    return sorted(result)
