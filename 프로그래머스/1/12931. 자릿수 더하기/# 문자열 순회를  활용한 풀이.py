# 제너레이터 표현식 문자열의 각 문자를 순회하면서 정수로 변환한 값들의 시퀀스를 생성
def solution(n):
    return sum(int(x) for x in str(n))
    
# 문자열 순회하는 방식 (위와 같은 방식_ 풀어쓴 것)
def solution2(n):
    sum = 0
    for x in str(n):
        sum += int(x)
    return sum
