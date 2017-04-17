/* 189e - Rotate Array
 *
 * My solutions were these:
 * (a) Brute force: Rotate one position at a time:
 *      O(nK) run time and O(1) space
 * (b) Maintain an array of length K that temporarily saves elements that
 * will be overwritten with the move.
 *      O(n) run time and O(K) space
 *
 * Below solution is from Discussion forum: O(n) and O(1)
 *
 * */
import java.util.*;

public class Solution {
    public void reverse(int[] A, int lo, int hi) {
        if(lo<0 || hi>A.length) return;

        while(lo<hi) {
            int tmp = A[lo];
            A[lo] = A[hi];
            A[hi] = tmp;
            lo++; hi--;
        }
    }

    public void rotate(int[] A, int K) {

        int sz = A.length;

        if(sz<2)    return;
        if(K==0)    return;

        K = K%sz;

        reverse(A, 0, sz-1);
        reverse(A, 0, K-1);
        reverse(A, K, sz-1);

        for(int i: A)
            System.out.print(i + " ");
        System.out.println();
    }

    public static void main(String[] a) {
        Solution s = new Solution();
        //int[] A = {1, 2, 3, 4, 5, 6, 7};
        //s.rotate(A, 3);
        //int[] B = {1, 2, 3, 4, 5, 6};
        //int[] B = {1, 2};
        int[] B = {1, 2};
        s.rotate(B, 1);
    }
}
