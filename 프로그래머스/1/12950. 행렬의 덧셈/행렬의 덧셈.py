# 못풀었음.;ㅋ
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for k in range(len(arr1[i])):
             arr1[i][k] += arr2[i][k]
        
    return arr1