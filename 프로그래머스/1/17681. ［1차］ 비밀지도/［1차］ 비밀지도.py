def solution(n, arr1, arr2):
    
    # 비트연산 쓰는거였구나..............
    # 적용해도 이 정도가 현실적일 듯..
    
    answer = []
    for i in range(n):
        temp = ''
        a = bin(arr1[i]|arr2[i])[2:]
        
        while len(a) < n:
            a = "0" + a
        
        a = a.replace('1', '#')
        a = a.replace('0', ' ')
        answer.append(a)
    return answer

def my_solution(n, arr1, arr2):
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]
    for i in range(n):
        while len(arr1[i]) < n:
            arr1[i] = "0" + arr1[i]
        while len(arr2[i]) < n:
            arr2[i] = "0" + arr2[i]
    
    answer = []
    for i in range(n):
        temp = ''
        for k in range(n):
            if (str(arr1[i])[k] == '0' and str(arr2[i])[k] == '0'):
                temp += ' '
            else :
                temp += '#'
        answer.append(temp)
    
    return answer