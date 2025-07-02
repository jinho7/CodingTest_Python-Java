class Solution {
    public long solution(int price, int money, int count) {
        // 총합 = (1*price + 2*price + ... n*price) = n! * price
        // n! * price - money
        long result = 0;
        for (int i = 1; i <= count; i++) result += i;
        // 단, 금액이 부족하지 않으면 0을 return 하세요.
        long answer = result*price - money;
        return answer < 0 ? 0 : answer;
    }
}