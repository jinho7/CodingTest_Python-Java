def solution(plans):
    for plan in plans:
        hour, minute = plan[1].split(":")
        plan[1] = int(hour) * 60 + int(minute)
        plan[2] = int(plan[2])
    plans.sort(key=lambda x: x[1])
    
    paused_assign = []
    result = []
    
    for i in range(len(plans) - 1):
        name, start, playtime = plans[i]
        next_start = plans[i+1][1]
        
        end_time = start + playtime
        if next_start >= end_time:
            result.append(name)
            free_time = next_start - end_time
            while paused_assign and free_time > 0:
                paused_name, remained_playtime = paused_assign.pop()
                if remained_playtime <= free_time:
                    result.append(paused_name)
                    free_time -= remained_playtime
                else:
                    paused_assign.append([paused_name, remained_playtime - free_time])
                    break
        else:
            real_playtime = next_start - start
            remained_playtime = playtime - real_playtime
            paused_assign.append([name, remained_playtime])
    
    # 마지막 과제 처리
    name, start, playtime = plans[-1]
    result.append(name)
    
    # paused_assign 처리
    while paused_assign:
        result.append(paused_assign.pop()[0])
    
    return result