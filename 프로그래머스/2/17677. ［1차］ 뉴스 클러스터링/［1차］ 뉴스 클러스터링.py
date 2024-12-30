def solution(str1, str2):

    # 전처리
    def preprocessing(string):
        # 모두 소문자로 통일
        lower_string = string.lower()
        temp = []
        result = []
        
        # 두 글자씩 끊기
        for i in range(len(lower_string)-1):
            temp.append(lower_string[i:i+2])
            
        # 영문만 추합
        for char in temp:
            if char.isalpha():
                result.append(char)
        
        return result
    
    pp_str1 = preprocessing(str1)
    pp_str2 = preprocessing(str2)
    
    c = len(pp_str1) + len(pp_str2)
    
    print(pp_str1)
    print(pp_str2)
    # 교집합
    a = 0
    for i in pp_str1:
        if i in pp_str2:
            pp_str2.remove(i)
            a += 1
            
    # 합집합
    b = c - a
    
    if b == 0:
        z = 1
    else:
        z = (a / b)

    # 자카드 유사도
    return int(z * 65536)