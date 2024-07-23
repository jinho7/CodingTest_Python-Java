def solution(s):
    # 이정도 경지에 이르렀다.
    return str(min([int(x) for x in s.split()])) + " " + str(max([int(x) for x in s.split()])) 