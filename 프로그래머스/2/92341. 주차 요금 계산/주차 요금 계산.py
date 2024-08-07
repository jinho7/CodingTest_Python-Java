import math

def solution(fees, records):
    # parking_time 에 각각 차량 번호 : 0 으로 만들어줌
    parking_time = {}
    for i in records:
        car_num = i.split(' ')[1]
        parking_time[car_num] = 0
    
    # 들어올 때 inside, 나갈때 del & 차이를 parking_time에 추가
    inside = {}
    for record in records:
        print("--------------------------------------------")
        time = record.split(' ')[0]
        car_num = record.split(' ')[1]
        in_or_out = record.split(' ')[2]
        
        minute = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
        #print("차량" , car_num , "가" , minute , "분에 찍힘")
        
        if in_or_out == 'IN':
            inside[car_num] = minute
        if in_or_out == 'OUT':
            parking_time[car_num] += minute - inside[car_num]
            del inside[car_num]
        #print("주차장에 있는 차 & 입장 시간 :" , inside)
        #print("누적 주차 시간 :" , parking_time)
        
    # 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
    for car_num, minute in inside.items():
        #print("[-------] 23:59에 출차된 것으로 간주 처리 [-------]")
        parking_time[car_num] += (23*60 + 59) - minute
        #print("누적 주차 시간 :" , parking_time)
    return [(fees[1] + math.ceil(max(0, value - fees[0]) / fees[2]) * fees[3]) for key, value in sorted(parking_time.items())]