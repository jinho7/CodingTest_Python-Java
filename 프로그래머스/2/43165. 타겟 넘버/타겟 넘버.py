def solution(numbers, target):
    answer = [0]  # list는 mutable이라 global/nonlocal 없이도 수정 가능
    
    def dfs(idx, sum_num):
        if idx == len(numbers):
            if sum_num == target:
                answer[0] += 1
            return
        dfs(idx + 1, sum_num + numbers[idx])
        dfs(idx + 1, sum_num - numbers[idx])
    
    dfs(0, 0)
    return answer[0]