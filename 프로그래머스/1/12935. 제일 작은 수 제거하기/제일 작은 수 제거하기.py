def solution(arr):
    arr.remove(sorted(arr, reverse=True).pop())
    return arr if arr else [-1]