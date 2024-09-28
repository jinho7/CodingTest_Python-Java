import math

def solution(m, n, startX, startY, balls):
    
    def calculate_distance_square(startX, startY, targetX, targetY):
        return (targetX-startX)**2 + (targetY-startY)**2
    
    def calculate_shortest_distance(startX, startY, targetX, targetY):
        candidate = []
        
        # 4 면 중 어디를 맞추는 것이 빠른가

        # x 축이 일치하지 않을 때만 진행
        if startX != targetX:
            # x 축에 대칭
            distance = calculate_distance_square(startX, startY, targetX, -targetY)
            candidate.append(distance)
            # y=n 에 대칭 
            distance = calculate_distance_square(startX, startY, targetX, n + (n-targetY))
            candidate.append(distance)
            
        # x 축이 같아도, 가능한 경우
        else:
            # startY가 작으면 -> x 축에 대칭 가능
            if startY < targetY:
                candidate.append((startY + targetY)**2)
            # startY가 크면 -> y=n 에 대칭  가능
            else:
                candidate.append((n- startY + n-targetY)**2)
            
        # y 축이 일치하지 않을 때만 진행
        if startY != targetY:
            # y 축에 대칭
            distance = calculate_distance_square(startX, startY, -targetX, targetY)
            candidate.append(distance)
            # x=m 에 대칭 
            distance = calculate_distance_square(startX, startY, m + (m-targetX), targetY)
            candidate.append(distance)
        # y 축이 같아도, 가능한 경우
        else:
            # startX가 작으면 -> y 축에 대칭 가능
            if startX < targetX:
                candidate.append((startX + targetX)**2)
            # startX가 크면 -> x=m 에 대칭  대칭 가능
            else:
                candidate.append((m- startX + m-targetX)**2)
            
            
        # 4개의 대각선 중 어디를 맞추는 것이 빠른가
            # 대각선으로 갔다가 올 때 있다는 건 가다가 부딪힌다는 뜻...
        return min(candidate)
    
    answer = []
    for ball in balls:
        targetX, targetY = ball
        shortest_distance = calculate_shortest_distance(startX, startY, targetX, targetY)
        answer.append(shortest_distance)
        
    return answer