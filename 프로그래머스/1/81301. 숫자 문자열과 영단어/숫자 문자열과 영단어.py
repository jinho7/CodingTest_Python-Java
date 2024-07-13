num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)




def my_solution(s):
    dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    answer = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
            i += 1
        elif s[i].isalpha():
            for length in range(3, 6):  # 영어 단어의 길이는 3에서 5까지의 범위로 가정
                word = s[i:i+length]
                if word in dic:
                    answer += dic[word]
                    i += length
                    break
    return int(answer)

def get_value_by_key(d, key):
    if key in d:
        return d[key]
    else:
        return None
    
