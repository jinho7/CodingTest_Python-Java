def solution(wallpaper):

    # x축 최대 최소 구하기
    cand_x = []
    for index in range(len(wallpaper)):
        if '#' in wallpaper[index]:
            cand_x.append(index)
    
    # y축 최소 최대 구하기
    cand_y = []
    for line in wallpaper:
        for index, item in enumerate(line):
            # 처음 '#'을 만나면 후보에 index를 추가하고 멈춘다.
            if item == '#':
                cand_y.append(index)
    
    return [min(cand_x), min(cand_y), max(cand_x)+1, max(cand_y)+1]