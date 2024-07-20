def solution(board, h, w):
    # board의 길이와 board[?]의 길이는 동일 -> n x n의 2차원 격자 판
    n = len(board)
    
    # 같은 색으로 색칠된 칸의 개수를 저장할 변수
    count = 0
    
    # 이동을 의미 (dh와 dw를 조합하여 0,1 / 1,0 / -1,0 / 0,1 을 모두 만들 수 있음)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    
    return count