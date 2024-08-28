import math
from itertools import permutations

def solution(n, k):
    # 기본 순열
    nums = [i+1 for i in range(n)]

    perm = []
    
    # 인덱스로 변환
    k -= 1
    
    # 순열을 결정할 때까지 루프
    while n > 0:
        # 총 개수 = 6개
        make_line_num = math.factorial(n)
        
        # 총 개수 // n = 6 // 3 = 2 (2개씩 나눠짐-> 11 22 33)
        num = make_line_num // n
        
        # 첫 번째 숫자 구하기.
        # index = 4 // 2 = 2
        # 즉, 3이 선택
        index = k // num
                
        # nums에서 해당 index에 있는 숫자를 꺼내어 perm에 추가
        perm.append(nums.pop(index))
        
        # print(perm, nums)
        
        # 4 % 2 -> 다음에는 0 번째 인덱스 
        k %= num
        
        # n을 감소시켜 다음 자릿수로 넘어감
        n -= 1
    
    return perm