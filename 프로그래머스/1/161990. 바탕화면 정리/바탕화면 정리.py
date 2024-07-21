def solution(wallpaper):
    
    
    # y축 최소 최대 구하기
    candidate = []
    for line in wallpaper:
        for index, item in enumerate(line):
            # 처음 '#'을 만나면 후보에 index를 추가하고 멈춘다.
            if item == '#':
                candidate.append(index)
    # 그 중 제일 작은 것이 y축 최소값
    luy = min(candidate)
    # 그 중 제일 큰 것 +1 이 y축 최대값
    rdy = max(candidate)+1
    
    # x축 최대 최소 구하기
    candidate = []
    for index in range(len(wallpaper)):
        if '#' in wallpaper[index]:
            candidate.append(index)
    lux = min(candidate)
    rdx = max(candidate)+1
    
    return [lux, luy, rdx, rdy]