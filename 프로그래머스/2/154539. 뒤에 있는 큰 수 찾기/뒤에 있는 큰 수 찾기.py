def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 결과 배열을 -1로 초기화
    stack = []

    for i in range(n - 1, -1, -1):  # 배열을 뒤에서부터 순회
        while stack and stack[-1] <= numbers[i]:
            stack.pop()  # 현재 원소보다 작거나 같은 값 제거
            
        if stack:
            answer[i] = stack[-1]  # 스택의 top이 뒷 큰수
        
        stack.append(numbers[i])  # 현재 원소를 스택에 추가

    return answer