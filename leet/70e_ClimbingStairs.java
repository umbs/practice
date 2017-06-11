public class Solution {
    int[] dp;
    
    public int util(int n) {
        if(dp[n] != -1) return dp[n];
        
        dp[n] = util(n-1) + util(n-2);
        
        return dp[n];
    }

    public int climbStairs(int n) {
        dp = new int[n+1];
        Arrays.fill(dp, -1);
        
        dp[0] = 1; dp[1] = 1;
        
        if(n<=1)    return dp[n];
        
        return util(n);
    }
}
