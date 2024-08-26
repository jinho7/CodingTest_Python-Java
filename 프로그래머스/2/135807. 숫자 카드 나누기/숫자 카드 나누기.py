import math

def gcd_of_list(lst):
    gcd_result = lst[0]
    for i in range(1, len(lst)):
        gcd_result = math.gcd(gcd_result, lst[i])
    return gcd_result

def solution(arrayA, arrayB):
    gcd_A = gcd_of_list(arrayA)
    gcd_B = gcd_of_list(arrayB)
    
    # 조건 1: gcd_A가 arrayB의 모든 원소를 나누지 못하는지 확인
    if all(b % gcd_A != 0 for b in arrayB):
        result_A = gcd_A
    else:
        result_A = 0
    
    # 조건 2: gcd_B가 arrayA의 모든 원소를 나누지 못하는지 확인
    if all(a % gcd_B != 0 for a in arrayA):
        result_B = gcd_B
    else:
        result_B = 0
    
    return max(result_A, result_B)
