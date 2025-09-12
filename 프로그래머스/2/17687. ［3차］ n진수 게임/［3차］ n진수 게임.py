def solution(n, t, m, p):
    # n 진법, t result 갯수, m 참가인원, 튜브 순서 p
    answer = ''
    
    num = 17
    s = ''
    while num != 0:
        x = num % n
        s += str(x)
        num = num // n
    print(s)
    
    return answer