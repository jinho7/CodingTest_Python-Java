from collections import defaultdict

def solution(clothes):
    dictionary = defaultdict(int)
    result = 1
    
    for name, kind in clothes:
        dictionary[kind] += 1

    for value in dictionary.values():
        result *= (value + 1)
    
    return result - 1