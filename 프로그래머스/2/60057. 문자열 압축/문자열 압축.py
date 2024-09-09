def solution(s):
    result = []
    
    for steps in range(1, len(s)):
        lst = [s[i:i+steps] for i in range(0, len(s), steps)]
        
        # print(lst)
        temp_num = 1
        temp = lst[0]
        
        temp_str = ''
        
        last_str = ''
        for i in range(1, len(lst)):
            if len(lst[i]) == steps:
                # 전 글자와 같은 때
                if temp == lst[i]:
                    temp_num += 1
                # 같지 않을 때
                else:
                    # 1이 아닐 때만 숫자붙여줌
                    if (temp_num != 1):
                        temp_str += str(temp_num)+temp
                    else:
                        temp_str += temp
                    
                    # temp 재 선언
                    temp = lst[i]
                    temp_num = 1
                    
            # 마지막 글자 남으면
            elif len(lst[i]) != steps:
                last_str += lst[i]
        # 1이 아닐 때만 숫자붙여줌
        if (temp_num != 1):
            temp_str += str(temp_num)+temp
        else:
            temp_str += temp
        result.append(len(temp_str+last_str))
        # print(temp_str+last_str)
    return min(result) if result else 1