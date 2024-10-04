from itertools import product

def solution(user_id, banned_id):
    answer = []
    # 벤 당한 id 순회
    for ban in banned_id:
        temp = []
        start_index = []
        # 벤의 * 처리된 index 부분 추가
        for i in range(len(ban)):
            if ban[i] == '*':
                start_index.append(i)
        
        # user 순회
        for user in user_id:
            check_user = []
            # user 길이와 벤 당한 id의 길이 똑같으면 일단 후보로 둔다.
            if len(user) == len(ban):
                for j in range(len(user)):
                    # 그리고, 벤의 * 처리된 index 부분 -> user_id의 index를 *처리
                    if j in start_index:
                        check_user.append('*')
                    else:
                        check_user.append(user[j])
                if (''.join(check_user)) == ban:
                    if user not in temp:            
                        temp.append(user)

        answer.append(temp)
    
    # 중복 제거를 위한 set
    valid_combinations = set()

    # 가능한 모든 조합에 대해 중복 제거 및 유효성 검사
    for case in product(*answer):
        if len(set(case)) == len(case):  # 동일한 사용자가 중복 매칭되지 않도록 함
            sorted_case = tuple(sorted(case))  # 순서 고려 없이 중복 제거
            valid_combinations.add(sorted_case)
    
    return len(valid_combinations)