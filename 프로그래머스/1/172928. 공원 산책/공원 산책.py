def solution(park, routes):
    # 싸그리 검색해서 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start = [i, j]
    
    # 현재 위치
    current = start
    
    # 방향에 따른 이동
    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    for route in routes:
        # 방향
        direction = route.split()[0]
        # 거리
        distance = int(route.split()[1])
        
        # 명령을 수행하기 전에 이동 가능한지 확인
        temp = current.copy()
        can_move = True
        
        # 한 칸씩 이동
        for i in range(distance):
            next_x = temp[0] + directions[direction][0]
            next_y = temp[1] + directions[direction][1]
            
            # 1. 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
            # 0보다 작거나 맥스보다 크면 False로
            if next_x < 0 or next_x >= len(park) or next_y < 0 or next_y >= len(park[0]):
                can_move = False
                break
            
            # 2. 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
            # X를 만나면 False로
            if park[next_x][next_y] == 'X':
                can_move = False
                break
            
            # 다 넘어왔으면 최종 값 저장
            temp = [next_x, next_y]
        
        # 이동 가능하면 위치 업데이트
        if can_move:
            current = temp
    
    return current