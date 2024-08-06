def solution(msg):
    # 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    dictionary = { chr(i+65) : i+1 for i in range(26)}

    answer = [0]
    addnum = 26
    temp = ""
    for i in range(len(msg)):
        temp += msg[i]
        
        if temp not in dictionary:
            addnum += 1
            dictionary[temp] = addnum
            temp = msg[i]
            answer.append(dictionary[temp])
            #print("없" + temp)
            
        else:
            answer[-1] = dictionary[temp]
            #print("있" + temp)
            
    return answer