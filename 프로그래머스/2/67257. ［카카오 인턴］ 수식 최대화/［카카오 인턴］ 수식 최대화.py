import math
from itertools import permutations
def solution(expression):
    # 피연산자
    operand = []
    # 연산자
    operator = []
    
    temp_operand = ""
    for char in expression:
        if char in "+-*":
            # 연산자 처리
            operator.append(char)
            # 피연산자 처리
            operand.append(int(temp_operand))
            temp_operand = ""
        else:
            temp_operand += char
            
    # 마지막 피연산자 처리
    operand.append(int(temp_operand))
    print(operand, operator)
    # [100, 200, 300, 500, 20] ['-', '*', '-', '+']
    
    # 연산자 우선 순위 종류
    operator_priority = list(permutations(set(operator)))
    print(operator_priority)
    # [('+', '*', '-'), ('+', '-', '*'), ('*', '+', '-'), ('*', '-', '+'), ('-', '+', '*'), ('-', '*', '+')]
    
    def calculate(op1, op2, operator):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
    

    max_result = 0
    
    # 각 우선순위에 대해 계산
    for priority in operator_priority:
        # 이거 또 실수함. 얕은 복사는 [:]
        temp_operand = operand[:]
        temp_operator = operator[:]
        
        for op in priority:
            while op in temp_operator:
                idx = temp_operator.index(op)
                
                # 해당 연산을 수행하고 피연산자와 연산자 리스트 갱신
                result = calculate(temp_operand[idx], temp_operand[idx + 1], op)
                temp_operand[idx] = result
                del temp_operand[idx + 1]
                del temp_operator[idx]
        
        # 결과의 절댓값을 구하고 최댓값 갱신
        max_result = max(max_result, abs(temp_operand[0]))
    
    return max_result