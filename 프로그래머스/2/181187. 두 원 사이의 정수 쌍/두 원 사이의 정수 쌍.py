import math
def solution(r1, r2):
    count = 0
    for y in range(0, r2 + 1):  # y좌표를 0부터 r2까지 반복
        x_max = math.floor(math.sqrt(r2**2 - y**2))
        x_min = math.ceil(math.sqrt(max(0, r1**2 - y**2)))
        count += x_max - x_min + 1
    
    return count * 4 - (r2 - r1 + 1) * 4