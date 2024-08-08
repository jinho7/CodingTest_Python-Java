# 누적합을 사용

# a b c d
# e f g h 가 있을 때,

# e에 b,c,d 중 최대값을 더해주고,
# f에 a,c,d 중 최대값을 더해주고,
# g에 a,b,d 중 최대값을 더해주고,
# h에 a,b,c, 중 최대값을 더해준다.
# 역설적으로 아래에서부터 가능한 수를 올라간다. 나비효과 느낌.

def solution(land):
    
    for i in range(1, len(land)):
        current_row = land[i]
        previous_row = land[i-1]
        for k in range(4):
            current_row[k] += max(previous_row[:k] + previous_row[k+1:])

    return max(land[-1])


# 그리디 적용 ㅣ 현재 선택이 다음 행의 선택을 제한하므로, 장기적으로 더 낮은 점수를 얻을 수 있다.
def greedy_solution(land):
    
    max_num = max(land[0])
    answer = max_num
    temp_index = land[0].index(max_num)
    
    
    for row in land[1:]:
        # 이전 index는 -1 처리 : 어차피 나머지 값들 다 자연수
        row[temp_index] = -1
    
        max_num = max(row)
        answer += max_num
        temp_index = row.index(max_num)

    return answer