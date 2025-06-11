import java.util.*;

class Solution {
    public long solution(long n) {
        // {String, String, ... } 으로 담아주고 sb에서 reverse 쓰기
        String[] st = String.valueOf(n).split("");
        Arrays.sort(st);
        StringBuilder sb = new StringBuilder();
        for (String s : st) sb.append(s);
        return Long.parseLong(sb.reverse().toString());
    }
}