/* Given a set of integers (non-negative) and a target sum, find number of ways
 * of inserting + and - symbols between the numbers such that the expression
 * results to target sum.  */
int findTargetSumWays(int* nums, int numsSize, int S) {
    if(numsSize==0 && S==0) return 1;   // found a valid combo
    if(numsSize==0 && S!=0) return 0;   // invalid combo
    
    int ways = 0;
    
    ways = findTargetSumWays(&nums[1], numsSize-1, S-nums[0]) + 
            findTargetSumWays(&nums[1], numsSize-1, S+nums[0]);
            
    return ways;
}
