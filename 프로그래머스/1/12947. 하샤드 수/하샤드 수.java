class Solution {
    public boolean solution(int x) {
       
        
        // 문자열로 바꾼 뒤 
        String y = Integer.toString(x);
        Integer sum = 0;
        
        for (int i = 0; i < y.length(); i++) {
            sum += y.charAt(i) - '0';

        }
        
        boolean answer;
        if (x % sum == 0) {
            answer = true;
        } else {
            answer = false;
        }
        
        return answer;
    }
}