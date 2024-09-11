import math

def solution(k, d):
    count = 0
    for a in range(0, d // k + 1):  # a는 k의 배수로 0부터 d // k 까지
        # b의 가능한 최대 값을 구함
        max_b = math.isqrt(d**2 - (a * k)**2) // k
        count += (max_b + 1)  # 가능한 b의 개수를 더함 (0부터 max_b까지)

    return count
