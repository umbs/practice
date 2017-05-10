/* 357m
 *
 * Given a non-negative number n, count all numbers x between 0 and 10^n
 * containing unique digits
 *
 * If n=2, there are 91 numbers with unique digits
 *
 * n=0, 1
 * n=1, 10 
 * n=2, 91
 * etc
 * */


public class Solution {
    /* 1 - 10 
     * 2 - 9 * 9
     * 3 - 9 * 9 * 8
     * 4 - 9 * 9 * 8 * 7
     * and so on
     * 10^n = 9 * 9 * 8 * 7 .. up to (10-n)
     */
    public int countNumbersWithUniqueDigits(int n) {
        if(n==0)    return 1;
        
        int[] uniqueForN = new int[10];
        int sum = 0;
        uniqueForN[0] = 10; uniqueForN[1] = 9 * 9;
        for(int i=2; i<10; i++) {
            uniqueForN[i] = uniqueForN[i-1] * (10-i);
        }
        
        for(int i=0; i<n; i++) {
            sum += uniqueForN[i]; 
        }
        
        return sum;
    }
}
