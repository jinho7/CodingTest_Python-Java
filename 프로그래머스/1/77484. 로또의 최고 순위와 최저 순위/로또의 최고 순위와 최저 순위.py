# 최저 / 최대 순위 구하기
def solution(lottos, win_nums):
    
    lottos.sort()
    win_nums.sort()
    caculate(lottos, win_nums)
    max_correct = caculate(lottos, win_nums)[0]+caculate(lottos, win_nums)[2]
    min_correct = caculate(lottos, win_nums)[0]
    return [rank(max_correct), rank(min_correct)]

    # for i in range(len(lottos)):
    #     if lottos[i]==0:
    #         print("")
    # return 

def caculate(arr1, answer):
    answer1 = answer.copy()
    correct = 0
    uncorrect = 0
    zero = 0
    # 역순으로 순회
    for a in range(len(arr1)-1, -1, -1):
        if arr1[a] in answer1:
            answer1.pop(a)
            correct += 1
        elif arr1[a] not in answer1:
            if arr1[a] == 0:
                zero += 1
            else:
                uncorrect += 1
    return correct, uncorrect, zero

def rank(int):
    if int == 0:
        return 6
    else:
        return 7-int