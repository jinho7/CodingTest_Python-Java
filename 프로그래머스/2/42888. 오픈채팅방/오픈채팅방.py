def solution(record):
    answer = []
    
    uid_nickname = {}
    for rec in record:
        history = rec.split()
        if history[0] == 'Enter' or history[0] == 'Change':
            uid_nickname[history[1]] = history[2]
    
    for rec in record:
        history = rec.split()
        if history[0] == 'Enter':
            nickname = uid_nickname[history[1]]
            string = f'{nickname}님이 들어왔습니다.'
            answer.append(string)
        if history[0] == 'Leave':
            nickname = uid_nickname[history[1]]
            string = f'{nickname}님이 나갔습니다.'
            answer.append(string)
    return answer