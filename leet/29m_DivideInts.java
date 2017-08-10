/* 29m - Divide Two Ints
 * Without using multiplication, division or mod operation, divide two
 * integers. The site is very low on details (negatives numbers?)
 */
import java.util.*;

public class Solution {

    public int divide(int up, int down) {
        int neg = 1;

        if(up==0)       return 0;
        if(up==down)    return 1;
        if(up==-down)   return -1;
        if(down==1)     return up;
        if(down==-1) {
            if(up==Integer.MIN_VALUE)
                return Integer.MAX_VALUE;
            return -up;
        }

        if((up<0 && down>0) || (up>0 && down<0))    neg = -1;

        up = Math.abs(up);
        down = Math.abs(down);

        int res = 0;
        while(up>0) {
            up -= down;
            res++;
            if(res==Integer.MAX_VALUE)  {
                System.out.println("Int Max");
                return Integer.MAX_VALUE;
            }
        }
        res--;

        return neg*res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.divide(-17,3));
        System.out.println(s.divide(-1,1));
        System.out.println(s.divide(-2147483648,-1));
    }
}
