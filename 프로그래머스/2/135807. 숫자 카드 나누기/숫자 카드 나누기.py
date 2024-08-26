import math

def gcd_list(lst):
    gcd_result = lst[0]
    for i in range(1, len(lst)):
        gcd_result = math.gcd(gcd_result, lst[i])
    return gcd_result

def solution(arrayA, arrayB):
    gcd_A = gcd_list(arrayA)
    gcd_B = gcd_list(arrayB)

    result_A = 0
    result_B = 0
    
    # 조건 1: gcd_A가 arrayB의 모든 원소를 나눌 수 없는지 확인
    is_valid_A = True
    for b in arrayB:
        if b % gcd_A == 0:
            is_valid_A = False
            break
    if is_valid_A:
        result_A = gcd_A
    
    # 조건 2: gcd_B가 arrayA의 모든 원소를 나눌 수 없는지 확인
    is_valid_B = True
    for a in arrayA:
        if a % gcd_B == 0:
            is_valid_B = False
            break
    if is_valid_B:
        result_B = gcd_B
    
    # 두 값 중 큰 값을 반환
    return max(result_A, result_B)