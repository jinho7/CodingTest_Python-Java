def solution(n):
    digits = "124"
    
    answer = ''
    while n > 0:
        answer += digits[(n - 1) % 3]
        n = (n - 1) // 3 
    
    return answer[::-1]