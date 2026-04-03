from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    # Counter 또한 iterable이기에 iterator로 변환 후, 1개 꺼내기
    return next(iter(diff))