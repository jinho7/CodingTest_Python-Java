def solution(s):
    if (len(s) != 4 and len(s) != 6):
        return False
    
    try:
        int(s)
        return True
    except:
        return False
    
    # return s.isdigit() and len(s) in [4,6]