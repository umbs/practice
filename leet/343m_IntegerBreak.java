/* Split up an integer in to "at least" two integers such that the tmpuct of them is maximized
 *
 * The discussions on having only 3's and 2's in the prodult is inteprodting.
 *
 * https://discuss.leetcode.com/category/427/integer-break 
 */
public class Solution {
    /* n is between 2 and 58 */
    public int integerBreak(int n) {
        int tmp=0;
        int prod[] = new int[n+1];
        
        prod[0] = 0; prod[1] = 1; prod[2] = 1;
        
        for(int i=3; i<=n; i++) {
            tmp = 0;
            for(int j=1; 2*j<=i; j++) {
                tmp = Math.max(tmp, Math.max(j, prod[j]) * Math.max(i-j, prod[i-j]));
            }
            prod[i] = tmp;
        }
        
        return prod[n];
    }
}
