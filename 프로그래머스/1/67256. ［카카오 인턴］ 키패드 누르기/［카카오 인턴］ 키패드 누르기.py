def solution(numbers, hand):
    
    # dictionay에 각 키를 2차원 배열로 치환하여 저장
    keypad_coords = {
        '1': [0, 3], '2': [1, 3], '3': [2, 3],
        '4': [0, 2], '5': [1, 2], '6': [2, 2],
        '7': [0, 1], '8': [1, 1], '9': [2, 1],
        '*': [0, 0], '0': [1, 0], '#': [2, 0]
    }
    numbers_coord = [keypad_coords[str(num)] for num in numbers]
    # print(numbers)
    # print(numbers_coord)
    
    result = ''
    left , right = [0,0], [2,0]
    for i in range(len(numbers)):
        # 1, 4, 7
        if numbers[i] in [1, 4, 7]:
            left[0], left[1] = numbers_coord[i][0], numbers_coord[i][1]
            result += 'L'
        # 3, 6, 9
        elif numbers[i] in [3, 6, 9]:
            right[0], right[1] = numbers_coord[i][0], numbers_coord[i][1]
            result += 'R'
        # 2, 4, 8, 0
        else:
            # 거리 계산
            distance_from_left = distance_calculate(left, numbers_coord[i])
            distance_from_right = distance_calculate(right, numbers_coord[i])
            # 같으면 어느손잡이 인지에 따라
            if distance_from_left == distance_from_right:
                if hand == "left":
                    left[0], left[1] = numbers_coord[i][0], numbers_coord[i][1]
                    result += 'L' 
                else :
                    right[0], right[1] = numbers_coord[i][0], numbers_coord[i][1]
                    result += 'R'
            # 왼손이 더 가까울 경우
            elif distance_from_left < distance_from_right:
                left[0], left[1] = numbers_coord[i][0], numbers_coord[i][1]
                result += 'L' 
            # 오른손이 더 가까울 경우
            else:
                right[0], right[1] = numbers_coord[i][0], numbers_coord[i][1]
                result += 'R'
    
    return result

def distance_calculate(current, target):
    return abs(current[0] - target[0]) + abs(current[1] - target[1])