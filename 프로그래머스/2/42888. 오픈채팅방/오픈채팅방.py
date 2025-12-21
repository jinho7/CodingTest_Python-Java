from collections import defaultdict

def solution(record):
    
    nickname_dict = defaultdict(str)
    answer = []
    
    for rec in record:
        action = rec.split()[0]
        if action == 'Enter' or action == 'Change':
            _, uid, nickname = rec.split()
            nickname_dict[uid] = nickname
    # print(nickname_dict)
    
    for rec in record:
        action = rec.split()[0]
        if action == 'Enter':
            _, uid, nickname = rec.split()
            answer.append(f'{nickname_dict[uid]}님이 들어왔습니다.')
        elif action == 'Leave':
            _, uid = rec.split()
            answer.append(f'{nickname_dict[uid]}님이 나갔습니다.')
    
    return answer