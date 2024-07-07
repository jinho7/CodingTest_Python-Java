def solution(arr):
    arr.remove(sorted(arr, reverse=True).pop())
    # arr.remove(min(arr))
    return arr if arr else [-1]
