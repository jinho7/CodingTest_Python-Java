def solution(elements):
    n = len(elements)
    circular_elements = elements * 2
    sum_set = set()
    for i in range(1, n + 1):
        # print(f"길이가 {i}인 연속 부분 수열")
        for j in range(0, n):
            sum_set.add(sum(circular_elements[j: j + i]))
    return len(sum_set)