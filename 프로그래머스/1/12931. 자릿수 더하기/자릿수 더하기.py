def solution(n):
    
    if (n <= 0 or n > 100000000):
        print ("N의 범위는 100,000,000 이하의 자연수로 제한합니다.")
        return None
    else : 
        count = len(str(n))
        a = 0
    
        while count > 0:
            a += (n%10)
            n //= 10
            count -= 1
        
        return a
    