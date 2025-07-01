import java.util.*;

class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i = left; i < right+1; i++) {
            // 약수의 개수가 짝수이다. = i의 제곱근이 정수가 아니다.
            answer += (Math.sqrt(i) != (int)Math.sqrt(i)) ? i : -i; 
        }
        return answer;
    }
}