from itertools import permutations

def solution(expression):
    
    # expression에 있는 모든 연산자, 피연산자 추출
    operations = []
    expression_to_list = []
    temp = ""
    for i in expression:
        if i.isdigit():
            temp += i
        if not i.isdigit():
            # 순열 조합 용으로 따로 연산자만
            operations.append(i)
            expression_to_list.append(temp)
            expression_to_list.append(i)
            temp = ""
    expression_to_list.append(temp)
    
    # 해당 연산자들로 모든 순열 조합 완성
    operations_priority = list(permutations(list(set(operations))))
    print(operations_priority)
    print(expression_to_list)
    answer = []
    
    def calculate(op, x, y):
        # 곱셈
        if op == "*":
            return str(int(x) * int(y))
        # 덧셈
        elif op == "+":
            return str(int(x) + int(y))
        # 빼기
        elif op == "-":
            return str(int(x) - int(y))

    # 순열 조합에 따른 연산 수행
    for op in operations_priority:
        # 얕은 복사
        temp_expression = expression_to_list[:]
        
        # 우선순위 순서대로 체크!
        for current_op in op:
            # temp_expression에 current_op가 없을 때까지 반복
            while current_op in temp_expression:
                idx = temp_expression.index(current_op)
                result = calculate(temp_expression[idx], temp_expression[idx-1], temp_expression[idx+1])
                temp_expression[idx-1:idx+2] = [result]
        
        # 계산된 결과를 answer 리스트에 추가
        answer.append(abs(int(temp_expression[0])))
    
    # 가장 큰 절대값 반환
    return max(answer)