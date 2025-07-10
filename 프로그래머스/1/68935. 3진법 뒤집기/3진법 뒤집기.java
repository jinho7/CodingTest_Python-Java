import java.util.*;

class Solution {
    public int solution(int n) {
        StringBuilder sb = new StringBuilder();
        sb.append(n % 3);
        while (n >= 3) {
            n = (int)(n / 3);
            sb.append(n % 3);
        }
        char[] ch = sb.toString().toCharArray();
        int answer = 0;
        for (int i = 0; i < ch.length; i++) answer += ((ch[i] - '0') * Math.pow(3, ch.length-i-1));
        return answer;
    }
}