def solution(n, left, right):
    answer = []
    # 전체 배열을 생성하지 않고 left부터 right까지의 요소만 출력하는 방법 고민
    for i in range(left, right+1):
        row = i // n
        column = i % n
        if row >= column:
            answer.append(row+1)
        else:
            answer.append(column+1)
    return answer

# 7, 14

# 1 2 3 4
# 2 2 3 /4
# 3 3 3 4
# 4 4 4/ 4
