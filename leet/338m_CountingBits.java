/* 338m - Counting bits
 * Given a non-negative number N, return number of set bits in each number i
 * from 0 to N in an array
 *
 * if N=5, return [0, 1, 1, 2, 1, 2]
 */
import java.util.*;

public class Solution {
    // Given an array of containings set bits for 0 to num-1, return set
    // bits for num
    public int bitsOfNum(int[] bits, int[] twos, int num) {
        int res=0;

        if(twos[num]==num)  return 1;

        while(num>0) {
            res += bits[twos[num]];
            num -= twos[num];
        }

        return res;
    }

    public int[] countBits(int num) {

        int[] res = new int[num+1];
        int[] twos = new int[num+1];
        int pw=2;

        // base case
        if(num==0) { res[0] = 0; return res; }
        if(num==1) { res[0]=0; res[1] = 1; return res; }

        res[0] = 0; res[1] = 1;
        twos[0] = 0; twos[1] = 1;

        // construct twos array
        for(int i=2; i<=num; i++) {
            if(pw*2<=i)  pw *= 2;
            twos[i] = pw;
        }

        for(int i=2; i<=num; i++) {
            res[i] = bitsOfNum(res, twos, i);
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
