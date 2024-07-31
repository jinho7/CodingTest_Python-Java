def solution(want, number, discount):
    
    wanted_dict = {x : y for x,y in zip(want,number)}
    
    count = 0
    for i in range(len(discount)-10 + 1):
        #print(str(i+1) + "번째 날 ----------------")
        temp = discount[i:i+10]
        goods_amount_dict = { item : temp.count(item) for item in temp}
        match = True
        #print(goods_amount_dict)
        for item in wanted_dict.keys():
            #print(item + "에 대해여")
            try :
                if wanted_dict[item] <= goods_amount_dict[item]:
                    #print("만족!", wanted_dict[item], goods_amount_dict[item])
                    None
                else :
                    #print("적어서 불만족!", wanted_dict[item], goods_amount_dict[item])
                    match = False
            except KeyError:
                #print("없어서 불만족!")
                match = False
                break;
        if match == True:
            count += 1 
    return count