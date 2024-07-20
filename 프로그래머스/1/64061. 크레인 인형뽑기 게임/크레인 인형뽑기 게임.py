def solution(board, moves):
    # 배열 재정의
    board = rearrange_board(board)
    print(board)
    
    basket = []
    count = 0
    
    for item in moves:
        # 해당 열이 비어있지 않다면
        if board[item-1]:
            # board의 item(=moves의 숫자)번 째 줄 맨 위에꺼 꺼내서 넣기
            basket.append(board[item-1][-1])
            # 꺼낸 것 처리
            del board[item-1][-1]
        # 그리고 바구니 같은 거 2개 쌓였나 체크
        if len(basket) >= 2 and check_same(basket):
            del basket[-2:]
            # 두개 씩 사라짐
            count += 2
    return count

# 상하를 기준으로 하나의 list로 생각 (크레인이 좌우로 움직이는 일은 없으므로)
# 변환
def rearrange_board(board):
    rows = len(board)
    cols = len(board[0])
    rearranged = [[] for _ in range(cols)]
    
    for col in range(cols):
        for row in range(rows-1, -1, -1):  # 아래에서 위로
            if board[row][col] != 0:
                rearranged[col].append(board[row][col])
    
    return rearranged


def check_same(arr):
    return True if arr[-2] == arr[-1] else False