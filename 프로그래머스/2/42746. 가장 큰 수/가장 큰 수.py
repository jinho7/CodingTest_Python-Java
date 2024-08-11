def solution(numbers):
    str_numbers = [str(num) for num in numbers]
    
    str_numbers.sort(key=lambda x: x*4, reverse=True)
    # 0만 처리 ex. 30 보다 3이 앞에 와야함. 1000이하 이므로, 000이 3개까지만 가능. 1000보다 1이 앞으로 와야함. -> 1111 > 1000100010001000
    answer = ''.join(str_numbers)
    
    return str(int(answer))  # 모두 0인거 제거