// Kadane's algo
// https://en.wikipedia.org/wiki/Maximum_subarray_problem

public class Solution {
    public int maxSubArray(int[] nums) {
        int lmax=nums[0], gmax=nums[0];
        
        for(int i=1; i<nums.length; i++) {
            // The main question that Kadane's algo cleverly addressed is how to
            // maintain subarray window, thus it's sum?
            // It uses a key insight in resetting start index of the window
            //
            // if lmax+x < x then reset the start and end index to current index
            // Otherwise add x to lmax and increment end index 
            lmax = Math.max(lmax+nums[i], nums[i]);
            gmax = Math.max(lmax, gmax);
        }
        
        return gmax;
    }
}
