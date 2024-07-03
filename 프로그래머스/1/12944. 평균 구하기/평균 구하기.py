def solution(arr):
    a = 0
    for i in range(len(arr)):
        a += arr[i]
    answer = a / len(arr)
    return answer

    # return sum(list) / len(list)