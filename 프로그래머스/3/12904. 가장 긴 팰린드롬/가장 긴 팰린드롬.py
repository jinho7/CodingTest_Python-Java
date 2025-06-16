def solution(s):
    answer = 0
    
    def check_palindrome(s):
        if s == s[::-1]:
            return True
        else:
            return False
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            if check_palindrome(s[i:j+1]):
                answer = max(answer, j+1-i)
            
    return answer