def solution(num_list):
    odd = ''
    even = ''
    
    # 홀수와 짝수 분리하여 이어 붙이기
    for num in num_list:
        if num % 2 == 0:
            even += str(num)  # 짝수는 even에 이어붙이기
        else:
            odd += str(num)   # 홀수는 odd에 이어붙이기
    
    # 이어 붙인 값을 정수로 변환 후 더하기
    return int(odd) + int(even)
