/* EPI problem? Not sure. Given an array of integers (positive and negative),
 * return max sum of a subarray. */
import java.util.*;

public class MaxSum{
    public static int maxSum(int[] A, int sz) {
        int maxSum = 0, Sum = 0;

        for (int i : A) {
            Sum += i;
            if (Sum < 0)    Sum = 0;
            maxSum = Math.max(maxSum, Sum);
        }

        return maxSum;
    }

    public static void main(String[] args) {
        MaxSum t = new MaxSum();
        int sz = 10;
        Random r = new Random();
        int[] A = new int[sz];
        
        final int RANGE_MAX = 10;
        final int RANGE_MIN = -10;

        // random numbers in range [-10,10)
        for (int i=0; i<sz; i++) A[i] = (r.nextInt(2*RANGE_MAX) - RANGE_MAX);
        for (int i=0; i<sz; i++) System.out.print(A[i] + " ");

        System.out.println("\nMax Sum: " + maxSum(A, sz));
    }
}
