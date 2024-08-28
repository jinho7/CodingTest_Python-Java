def split_balanced_string(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        elif p[i] == ')':
            count -= 1
        if count == 0:
            u = p[:i + 1]
            v = p[i + 1:]
            return u, v

# u가 최소단위이고, 이미 균형잡힌 괄호 문자열 일 경우 -> 올바른 괄호 문자열 = '(' 로 시작
def check_correct_case(u):
    if u:
        if u[0] == "(":
            return True
        else:
            return False

def make_correct_case(u):
    u = u[1:-1]
    temp = ""
    for char in u:
        if char == "(":
            temp += ")"
        else:
            temp += "("
    return temp
    
def solution(p):
    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if not p:
        return ""
    
    # 2. 문자열 p를 두 "균형잡힌 괄호 문자열" u, v로 분리
    u, v = split_balanced_string(p)
    
    # 3. u가 "올바른 괄호 문자열"이라면 v에 대해 1단계부터 재귀적으로 수행한 결과를 u에 이어 붙인 후 반환
    if check_correct_case(u):
        return u + solution(v)
    else:
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행
        return "(" + solution(v) + ")" + make_correct_case(u)