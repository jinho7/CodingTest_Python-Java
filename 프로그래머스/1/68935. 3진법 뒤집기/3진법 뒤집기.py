def solution(n):
    
    ternary = ""
    while n > 0:
        remainder = n % 3
        ternary = str(remainder) + ternary
        n = n // 3
        
    a = ''.join(reversed(ternary))
        
    return int(a, 3)
