class Solution {
    public int solution(int n) {
        int ans = 0;
        if (n%2==0) {
            for (int a = n;a>0;a--) {
                if (a%2==0) {
                    ans += a*a;
                }
            }
        }
        else {
            for (int a = n;a>0;a--) {
                if (a%2!=0) {
                    ans += a;
                }
            }
        }
        return ans;
    }
}