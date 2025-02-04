def solution(dots):
    # x 좌표와 y 좌표의 최소값과 최대값을 구함
    x_coords = [dot[0] for dot in dots]
    y_coords = [dot[1] for dot in dots]
    
    # 가로 길이와 세로 길이를 계산
    width = max(x_coords) - min(x_coords)
    height = max(y_coords) - min(y_coords)
    
    # 넓이를 반환
    return width * height
