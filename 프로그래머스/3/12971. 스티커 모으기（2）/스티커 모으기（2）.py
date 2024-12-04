def solution(sticker):
    # 일단 len(sticker) // 2 개는 뽑는 것이 무조건 베스트인가? NO
    # 100, 1, 2, 99, 1, 2 인 경우 100, 99 만 2개 뽑는 것이 이득.
    
    answer = 0
    if len(sticker) <= 2:
        return max(sticker)

    # 첫번째 스티커 선택
    dp1 = [0] * (len(sticker)-1)
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    # 첫번째 스티커 미선택
    dp2 = [0] * len(sticker)
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    return max(dp1[-1], dp2[-1])