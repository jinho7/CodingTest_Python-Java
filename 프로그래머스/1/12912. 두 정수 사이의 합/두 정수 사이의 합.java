class Solution {
    public long solution(int a, int b) {
        // 대소 관계 바로 잡기
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }
        
        long answer = 0;
        for (int i = a ; i <= b ; i++ ){
            answer += i;
        }
        return answer;
    }
}