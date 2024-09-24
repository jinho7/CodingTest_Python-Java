from itertools import combinations

def solution(line):
    
    # 교점 찾기
    intersection = set()
    for first_line, second_line in combinations(line, 2):
        A, B, E = first_line
        C, D, F = second_line
        
        if ((A*D - B*C) != 0):
            # 교점 계산
            x = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) / (A*D - B*C)
            
        # 둘 다 정수이면 추가
        if int(x) == x and int(y) == y:
            intersection.add((int(x), int(y)))
    
    # x와 y 값들의 최솟값과 최댓값 구하기
    intersection = [list(point) for point in intersection]
    #print(intersection)
    x_values = [x for x, y in intersection]
    y_values = [y for x, y in intersection]
    x_min, x_max = min(x_values), max(x_values)
    y_min, y_max = min(y_values), max(y_values)
    
    # x_min과 y_min을 0으로 만들기 (x를 -x_min, y를 -y_min 이동 )
    for i in range(len(intersection)):
        intersection[i][0] -= x_min
        intersection[i][1] -= y_min
    #print("변환된 교점 좌표들: ", intersection)
    # 최대 . 판 만들기
    board = [['.' for _ in range(x_max-x_min+1)] for _ in range(y_max-y_min+1)]
    #print(board)

    # 해당 좌표를 *로 바꿔주기
    # 세로가 인덱스상 뒤집혀 있음 -> y=1 이 그림상 맨 밑에 있는 구조
    # x, y 반대임 -> (3,1) = 마지막 째 바로 위줄의 첫번째 . 
    for x, y in intersection:
        board[y_max - y_min - y][x] = '*'
        
    return [''.join(row) for row in board]