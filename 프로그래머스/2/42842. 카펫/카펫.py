import math

def solution(brown, yellow):
    
    # 1) brown + yellow = x * y
    # 2) brown = 2(x-1) + 2(y-1)
    # 3) yellow = (x-2) * (y-2)
    
    # S = a*b = brown + yellow 면적의 해 a,b는 유일
    
    s = brown + yellow
    
    # 3부터 체크, S/i가 정수 아니면 넘겨도됨
    # 루트 S (정수) 까지 체크
    for i in range(3, int(math.sqrt(s))+1) :
        if s/i == s//i:
            x, y = (s//i), i
            if yellow == (x-2) * (y-2):
                return [x, y]
    return False