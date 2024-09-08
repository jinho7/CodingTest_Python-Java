import math
def solution(w,h):
    
    w_h_gcd = math.gcd(w,h)
    min_w = w // w_h_gcd
    min_h = h // w_h_gcd 
    
    # 가로 지나가는 수 + 세로 지나가는 수 - 꼭짓점 중복 제거
    min_pattern = min_w + min_h -1
    
    return w * h - (min_pattern * w_h_gcd)