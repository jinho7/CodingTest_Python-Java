def solution(numbers):
    return '0' if sum(numbers) == 0 else ''.join(sorted(list(map(str, numbers)), key= lambda x: x*4, reverse=True))