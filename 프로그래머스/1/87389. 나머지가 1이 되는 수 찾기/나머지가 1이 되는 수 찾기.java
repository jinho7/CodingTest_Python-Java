class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i < n ; i ++) {
            int k = n;
            if (k % i == 1) {
                answer = i;
                break;
            }
        }
        
        return answer;
    }
}