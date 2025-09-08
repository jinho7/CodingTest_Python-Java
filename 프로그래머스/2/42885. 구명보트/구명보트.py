from collections import deque

def solution(people, limit):
    x = deque(sorted(people))
    answer = 0
    while x:
        man_1 = x.pop()
        if x and x[0] + man_1 <= limit:
            x.popleft()
        answer += 1
    return answer
