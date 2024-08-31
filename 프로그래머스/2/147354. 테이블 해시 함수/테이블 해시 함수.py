def solution(data, col, row_begin, row_end):

    # -x : 내림차순
    # data = sorted(data, key=lambda x: (x[col], -x[0]))

    # 1. 첫 번째 컬럼을 기준으로 내림차순 정렬
    data.sort(key=lambda x: x[0], reverse=True)

    # 2. col번째 컬럼을 기준으로 오름차순 정렬
    data.sort(key=lambda x: x[col-1])
    
    result = []
    # print("정렬된 data : " , data)
    for i in range(row_begin, row_end+1):
        S = []
        for j in data[i-1]:
            temp = 0
            temp += j % (i)
            # print("각 S :" , j , "mod" , (i+1) , "=", j % (i))
            S.append(temp)
        result.append(sum(S))
    # print("총 S들 : ", result)
    answer = 0

    for value in result:
        answer ^= value
              
    return answer