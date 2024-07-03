def solution(s):
    if (s.startswith("0")):
        print("s는 0으로 시작할 수 없습니다.")
    elif (1<= len(s) <= 5):
        a = int(s)
        return(a)
    else:
        print("s의 길이는 1 이상 5이하입니다.")