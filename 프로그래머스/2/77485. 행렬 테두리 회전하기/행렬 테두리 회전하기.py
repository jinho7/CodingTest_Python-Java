def solution(rows, columns, queries):
    result = []
    
    # 행렬 생성
    matrix = [[(r * columns + c + 1) for c in range(columns)] for r in range(rows)]
    
    def rotate(x1, y1, x2, y2):
        # 순서대로 담아준다.
        temp = []
        
        # 상단 테두리
        for c in range(y1, y2 + 1):
            temp.append(matrix[x1][c])
        
        # 우측 테두리
        for r in range(x1 + 1, x2 + 1):
            temp.append(matrix[r][y2])
        
        # 하단 테두리
        for c in range(y2 - 1, y1 - 1, -1):
            temp.append(matrix[x2][c])
        
        # 좌측 테두리
        for r in range(x2 - 1, x1, -1):
            temp.append(matrix[r][y1])
        
        # 회전 = 시계 방향으로 1칸 이동
        temp = [temp[-1]] + temp[:-1]  
        
        # 회전된 테두리 값을 행렬에 반영
        idx = 0
        for c in range(y1, y2 + 1):
            matrix[x1][c] = temp[idx]
            idx += 1
        
        for r in range(x1 + 1, x2 + 1):
            matrix[r][y2] = temp[idx]
            idx += 1
        
        for c in range(y2 - 1, y1 - 1, -1):
            matrix[x2][c] = temp[idx]
            idx += 1
        
        for r in range(x2 - 1, x1, -1):
            matrix[r][y1] = temp[idx]
            idx += 1
        
        # 최소값
        min_val = min(temp)
        return min_val
    
    # 쿼리 처리
    for (x1, y1, x2, y2) in queries:
        # 인덱스값으로 바꿔주기
        min_val = rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1)
        result.append(min_val)
    
    return result
