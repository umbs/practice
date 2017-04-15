/* 413m - Arithmetic Slices */

import java.util.*;

public class Solution {

    /* Given a window/range, number of slices can be computed */
    public int sum(int i, int j) {
        int res=0;
        while(i<=j-2) {
            res+= j-i-1;
            i++;
        }

        return res;
    }

    public int numberOfArithmeticSlices(int[] A) {
        int diff=0, slices=0;

        if(A.length==1 || A.length==2)  return 0;

        for(int i=1, j=1; i<A.length; i=j) {
            diff = A[i]-A[i-1];

            /* Window of numbers with same diff */
            for(j=i; j<A.length && (diff==A[j]-A[j-1]); j++);

            slices += sum(i, j);
        }

        return slices;
    }

    public static void main(String[] a) {
        Solution s = new Solution();
        int[] A = {1, 2, 3, 4, 5, 6};
        System.out.println(s.numberOfArithmeticSlices(A));
        int[] B = {1, 1, 1, 2, 3, 4};
        System.out.println(s.numberOfArithmeticSlices(B));
        int[] C = {1, -1, -3, 0, 3, 6};
        System.out.println(s.numberOfArithmeticSlices(C));
        int[] D = {1, 1, 2, 5, 7};
        System.out.println(s.numberOfArithmeticSlices(D));
    }
}
