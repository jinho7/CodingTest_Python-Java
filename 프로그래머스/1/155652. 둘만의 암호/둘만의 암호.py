def solution(s, skip, index):
    # a 97, z 122 
    answer = ''
    for char in s:    
        current = ord(char)
        count = 0
        while count < index:
            current = (current + 1 - 97) % 26 + 97
            if chr(current) not in skip:
                count+=1
        answer += chr(current)
        
    return answer