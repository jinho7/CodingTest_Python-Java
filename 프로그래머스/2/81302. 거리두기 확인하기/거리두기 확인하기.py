import math

def solution(places):
    answer = []
    seat_dict = {}
    for i in range(len(places)):
        seat_dict[i+1] = []
    for i in range(len(places)):
        for j in range(len(places[0])):
            for k in range(len(places[0][0])):
                if places[i][j][k] == 'P':
                    seat_dict[i+1].append([j, k])
                    
    for i in range(len(places)):
        # (i+1) 강의실 체크
        print("---------", i+1, "번 째 강의실 ---------")
        room = places[i]
        person_seat = seat_dict[i+1]
        manhattan_check_list = []
        
        if check_manhattan(room, person_seat, manhattan_check_list):
            answer.append(1)
        else:
            answer.append(0)
    return answer

def check_manhattan(room, person_seat, manhattan_check_list):
    #print("강의실 배치 :", room)
    #print("수강생 위치 리스트 :", person_seat)
    for i in range(len(person_seat)):
        for j in range(i+1, len(person_seat)):
            first, second = person_seat[i],person_seat[j]
            x1, y1 = first[0], first[1]
            x2, y2 = second[0], second[1]
            # 맨해튼 거리 1
            if abs(x1-x2) + abs(y1-y2) == 1:
                #print(x1,y1, "과", x2,y2, "의 맨해튼 거리 1 입니다.")
                return False
            
            # 맨허튼 거리 2
            if abs(x1-x2) + abs(y1-y2) == 2:
                #print(x1,y1, "과", x2,y2, "의 맨해튼 거리 2 입니다.")
                # 직선 ; 자리 사이에 파티션 존재
                    # (x좌표 서로 같음 -> y 좌표 사이 체크)
                if x1 == x2:
                    if room[x1][(y1+y2)//2] == "X" :
                        continue
                    else:
                        return False
                    # (y좌표 서로 같음 -> x 좌표 사이 체크)
                elif y1 == y2:
                    if room[(x1+x2)//2][y1] == "X" :
                        continue
                    else:
                        return False
                # 대각선 ; 양 사이에 파티션 2개 있음
                else:
                    if room[x1][y2] == "X" and room[x2][y1] == "X":
                        continue
                    else:
                        return False
                    
            # 맨허튼 거리 2 이상
            else:
                #print(x1,y1, "과", x2,y2, "의 맨해튼 거리 2 이상 입니다.")
                continue
    return True
                