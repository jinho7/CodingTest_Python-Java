# dfs보다 수학적으로
# 1. 일단 X가 더 숫자가 많을 수는 없음. O가 많아도 하나 많거나 같아야함. 
# 2. 동시에 이길 수는 없음 (누군가 이겼다면 그 순간 끝나야 함)
# 3. O가 이겼을 때, O가 하나 더 많아야 함
# 4. X가 이겼을 때, 수가 똑같아야 함

# [O가 이겼거나, X가 이겨야 끝남.]
# 5. 이외에 아무도 이긴 사람이 없을 때, 1에서 안 걸러지면 그냥 통과

def solution(board):
    o_count = 0
    x_count = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                o_count += 1
            elif board[i][j] == "X":
                x_count += 1
            else:
                continue
                
    # 1번 : 초기에 숫자 체크
    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    def is_winner(player):
        # 가로 체크
        for i in range(3):
            # 가로 체크
            if board[i] == player*3:
                return True
            # 세로 체크
            elif board[0][i]+board[1][i]+board[2][i] == player*3:
                return True
        # 대각선 체크
        if board[0][0]+board[1][1]+board[2][2] == player*3 or board[0][2]+board[1][1]+board[2][0] == player*3:
                return True
        return False
    
    is_O_win = is_winner('O')
    is_X_win = is_winner('X')
    
    # 2번 : 동시에 우승 안됨
    if is_O_win and is_X_win :
        return 0
    
    # 3번
    if is_O_win and o_count != x_count + 1:
        return 0
    
    # 4번
    if is_X_win and o_count != x_count:
        return 0
    
    return 1