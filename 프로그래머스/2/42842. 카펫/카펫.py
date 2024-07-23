def solution(brown, yellow):
    # 최소 3x3
    # 전체 격자 수 = brown + yellow = w * h
    # 갈색 격자 수 = 2w + 2h - 4 (테두리)
    # 노란색 격자 수 = (w-2) * (h-2)
    total = brown + yellow
    
    # h 3부터 돌자.
    # 이것도 어차피 제곱근 까지만 돌면 됨 (h * w = total 이라)
    for h in range(3, int(total**0.5) + 1):
        # 나누어 떨어지면
        if total % h == 0:
            w = total / h
            if (w-2) * (h-2) == yellow:
                return [w, h]