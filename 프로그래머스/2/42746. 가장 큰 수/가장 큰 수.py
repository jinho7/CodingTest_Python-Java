def solution(numbers):
    str_numbers = [str(num) for num in numbers]
    
    str_numbers.sort(key=lambda x: x*4, reverse=True)
    answer = ''.join(str_numbers)
    
    return '0' if answer[0] == '0' else answer
