def solution(arr, divisor):
    result = [num for num in arr if (num % divisor == 0)]
    return sorted(result) if (result != []) else [-1]
# result != [] ; 비어 있지 않으면 그냥 true라 result라고 만 써도 됨