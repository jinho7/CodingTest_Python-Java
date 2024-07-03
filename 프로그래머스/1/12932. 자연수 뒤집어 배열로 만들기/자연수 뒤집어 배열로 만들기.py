def solution(n):
    answer = list(map(int, reversed(str(n))))
    return answer

def solution2(n):
    answer = list(map(int, (str(n)[::-1])))
    return answer