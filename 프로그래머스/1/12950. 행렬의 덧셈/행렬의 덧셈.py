# 못풀었음.;ㅋ
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        raw = []
        for k in range(len(arr1[i])):
             raw.append(arr1[i][k] + arr2[i][k])
        answer.append(raw)
    return answer