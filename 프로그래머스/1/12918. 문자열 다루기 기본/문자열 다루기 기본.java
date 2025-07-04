class Solution {
    public boolean solution(String s) {
        for (char ch : s.toCharArray()) {
            if (Character.isLetter(ch)) return false;
        }
        return s.length() == 4 || s.length() == 6 ? true : false;
    }
}