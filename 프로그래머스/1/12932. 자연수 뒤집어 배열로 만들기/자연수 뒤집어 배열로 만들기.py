# reversed 사용
def solution(n):
    answer = list(map(int, reversed(str(n))))
    return answer

# 슬라이싱 역순 사용
def solution2(n):
    answer = list(map(int, (str(n)[::-1])))
    return answer
