class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String ans1 = "";
        ans1 = Integer.toString(a) + Integer.toString(b);
        int ans2 = (a*b) * 2;
        if (ans2>Integer.parseInt(ans1)) return ans2;
        else return Integer.parseInt(ans1);
    }
}