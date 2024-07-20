# data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후,
# sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
def solution(data, ext, val_ext, sort_by):
    dic = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3} 
    
    new_item = []
    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑아서 넣기
    for item in data:
        if item[dic[ext]] < val_ext:
            new_item.append(item)

    return sorted(new_item, key=lambda x: x[dic[sort_by]])