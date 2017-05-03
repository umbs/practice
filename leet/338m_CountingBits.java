/* 338m - Counting bits
 * Given a non-negative number N, return number of set bits in each number i
 * from 0 to N in an array
 *
 * if N=5, return [0, 1, 1, 2, 1, 2]
 *
 * 0   0
 * 1   1
 * 2   1
 * 3   2
 * 4   1
 * 5   2
 * 6   2
 * 7   3
 * 8   1
 * 9   2
 * 10  2
 * 11  3
 * 12  2
 * 13  3
 * 14  3
 * 15  4
 * 16  1
 * 17  2
 * 18  2
 * 19  3
 * 20  2
 * 21  3
 * 22  3
 * 23  4
 * 24  2
 * 25  3
 */
import java.util.*;

public class Solution {
    public int[] countBits(int num) {

        int[] res = new int[num+1];
        int pw=1;

        // base case
        if(num==0) { res[0] = 0; return res; }
        if(num==1) { res[0]=0; res[1] = 1; return res; }

        res[0] = 0; res[1] = 1;

        // Set all power's of 2 to 1
        for(int i=1; i<32; i++) {
            int idx = (int)Math.pow(2, i);
            if(idx > num)   break;
            else            res[idx] = 1;
        }

        int twoPower = 2, rem;

        for(int i=2; i<=num; i++) {
            if(res[i]==1) {
                twoPower = i;
                continue;
            }

            rem = i-twoPower;
            res[i] = 1 + res[rem];
        }

        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] res = s.countBits(0);

        System.out.print("Bits: ");
        for(int i:res) {
            System.out.print(i + ", ");
        }
        System.out.println();
    }
}
