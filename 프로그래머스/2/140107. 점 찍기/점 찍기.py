def solution(k, d):
    count = 0
    for y in range(0, d + 1, k):  # d 값을 포함
        # x 좌표 구하기
        x = (d**2 - y**2)**0.5
        
        # x // k는 가능한 최대 x 좌표의 인덱스이므로, 여기에 +1을 추가해 포함
        # ex) x=12, k=3 이면 가능한 x 좌표 -> 0,3,6,9,12 = 5개
        count += int(x // k) + 1
    return count