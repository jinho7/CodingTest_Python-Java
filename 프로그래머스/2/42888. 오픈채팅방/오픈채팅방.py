def record_action(records, action, name):
    if action == "Enter":
        message = f"{name}님이 들어왔습니다."
    elif action == "Leave":
        message = f"{name}님이 나갔습니다."
    else:
        return
    records.append(message)

def solution(record):
    chatroom_history = []
    id_nick_dict = {}
    for i in record:
        try:
            action, user_id, nickname = i.split(' ')
            # Change도 처리 됨
            id_nick_dict[user_id] = nickname
            if action == 'Enter':
                
                chatroom_history.append([action, user_id])
        except ValueError:
            action, user_id = i.split(' ')
            chatroom_history.append([action, user_id])
    # print(chatroom_history)   
    answer = []
    for history in chatroom_history:
        record_action(answer, history[0], id_nick_dict[history[1]])

    return answer