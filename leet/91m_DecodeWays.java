/* Got this solution from Discussion forum. I failed after multiple attempts.
 *
 * The key insight here is using DP from tail to head (like a bottom up DP).
 *
 * */
public class Solution {
    public int numDecodings(String s) {
        if(s.isEmpty() || s==null)  return 0;

        int n = s.length();
        int[] dp = new int[n+1];

        dp[n] = 1;
        dp[n-1] = s.charAt(n-1)=='0' ? 0 : 1;

        for(int i=n-2; i>=0; i--) {
            if(s.charAt(i)=='0')    continue;
            dp[i] = Integer.parseInt(s.substring(i, i+2)) < 27 ?
                        dp[i+1]+dp[i+2] : dp[i+1];
        }

        return dp[0];
    }

    public static void main(String[] a) {
        Solution S = new Solution();
        System.out.println(S.numDecodings("11"));
    }
}

