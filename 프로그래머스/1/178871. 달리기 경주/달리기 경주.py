def solution(players, callings):
    # 선수 이름을 키로, 순위를 값으로 하는 딕셔너리
    rank_dict = {player: rank for rank, player in enumerate(players)}
    
    # 순위를 키로, 선수 이름을 값으로 하는 딕셔너리
    player_dict = {rank: player for rank, player in enumerate(players)}
    
    for name in callings:
        # 현재 선수의 순위
        current_rank = rank_dict[name]
        
        # 앞 선수의 순위와 이름
        prev_rank = current_rank - 1
        prev_player = player_dict[prev_rank]
        
        # 순위 교환
        rank_dict[name] = prev_rank
        rank_dict[prev_player] = current_rank
        
        # 선수 교환
        player_dict[prev_rank] = name
        player_dict[current_rank] = prev_player
    
    # 최종 순위대로 선수 이름 반환
    return [player_dict[i] for i in range(len(players))]