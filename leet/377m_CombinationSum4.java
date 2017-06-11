/* From discussion forums */
public class Solution {
    int[] dp;
    public int util(int[] nums, int target) {
        if(dp[target] != -1)    return dp[target];
        
        int res = 0;
        for(int i=0; i<nums.length; i++) {
            if(target < nums[i])    continue;
            res += util(nums, target-nums[i]);
        }
        dp[target] = res;
        return res;
    }
    
    public int combinationSum4(int[] nums, int target) {
        if(target <= 0) return 1;
        dp = new int[target+1];
        Arrays.fill(dp, -1);
        dp[0] = 1;
        return util(nums, target);
    }
}
