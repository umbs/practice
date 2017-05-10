/* Split up an integer in to "at least" two integers such that the product of them is maximized
 *
 * The discussions on having only 3's and 2's in the result is interesting.
 *
 * https://discuss.leetcode.com/category/427/integer-break 
 */
public class Solution {
    /* n is between 2 and 58 */
    public int integerBreak(int n) {
        int prod=0;
        int res[] = new int[n+1];
        
        res[0] = 0; res[1] = 1; res[2] = 1;
        
        for(int i=3; i<=n; i++) {
            prod = 0;
            for(int j=1; 2*j<=i; j++) {
                prod = Math.max(prod, Math.max(j, res[j]) * Math.max(i-j, res[i-j]));
            }
            res[i] = prod;
        }
        
        return res[n];
    }
}
