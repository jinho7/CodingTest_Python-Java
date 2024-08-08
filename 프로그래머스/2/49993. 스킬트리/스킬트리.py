def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_list = ''
        for s in skill_tree:
            if s in skill:
                skill_list += s
        # skill은 CBD인데, skill_list에 담긴건 CB일수도 있음.
        if skill.startswith(skill_list):
            answer += 1
    return answer