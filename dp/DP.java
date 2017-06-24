import java.util.*;

public class DP {

    /* Min Cost Path
     *
     * Input: A 2D array with cost of traveling through a cell and final
     * position/Cell.
     * Output: Determine the minimum cost of path from (0,0)/starting cell to
     * final cell
     *
     * */
    public int price[][];

    public int minCostHelper(int[][]cost, int n, int m) {
        if(n<0 || m<0)  return 0;
        if(n==0 || m==0)    return price[n][m];

        int x = minCostHelper(cost, n-1, m);
        int y = minCostHelper(cost, n-1, m-1);
        int z = minCostHelper(cost, n, m-1);

        return cost[n][m] + Math.min(x, Math.min(y, z));
    }

    public int minCost(int[][]cost, int n, int m) {
        int rows = cost.length;
        int col = cost[0].length;

        price = new int[rows][col]; // initialized to 0

        // initialize rows
        for(int r=0, sum=0; r<rows; r++) {
            sum += cost[r][0];
            price[r][0] = sum;
        }

        // initialize columns
        for(int c=0, sum=0; c<col; c++) {
            sum += cost[0][c];
            price[0][c] = sum;
        }

        return minCostHelper(cost, n, m);
    }

    /* Input: String a, String b
     * Output: Number of edits required to convert String a to String b
     *
     * L(a[0...n], b[0...m]):
     *  if(a[n]==b[m])  return L(a[0...n-1], b[0...m-1])
     *
     *  x = L(a[0...n], b[0...m-1]) // delete from b
     *  y = L(a[0...n-1], b[0...m]) // add to a
     *  z = L(b[0...n-1], b[0...m-1]) // replace
     *
     *  return min(x, y, z)
     *  */
    public int editDistance(String a, String b) {
        int alen = a.length(), blen = b.length();

        if(alen==0 || blen==0)  return 0;

        if(a.charAt(alen-1) == b.charAt(blen-1))
            return editDistance(a.substring(0, alen-1), b.substring(0, blen-1));

        int x = editDistance(a.substring(0, alen), b.substring(0,  blen-1));
        int y = editDistance(a.substring(0, alen-1), b.substring(0, blen));
        int z = editDistance(a.substring(0, alen-1), b.substring(0, blen-1));

        return 1+Math.min(x, Math.min(y, z));
    }

    /*
     * Input: String a, String b
     * Output: List<String> LCS // Longest Common Subsequence
     *
     * LCS(a[0...n-1], b[0...m-1])
     *  if (a[n-1] == b[m-1])
     *      return 1 + LCS(a[0...n-2], b[0...m-2])
     *  else
     *      return MAX(LCS(a[0...n-2], b[0...m-1]), LCS(a[0...n-1], b[0...m-2))
     */
    public StringBuilder lcs = new StringBuilder("");

    public int LCS(String a, String b) {
        int alen = a.length();
        int blen = b.length();

        if(alen==0 || blen==0)  return 0;

        if(a.charAt(alen-1)==b.charAt(blen-1)) {
            lcs.append(a.charAt(alen-1));
            return 1 + LCS(a.substring(0, alen-1), b.substring(0, blen-1));
        }

        return Math.max(LCS(a.substring(0, alen-1), b.substring(0, blen)),
                LCS(a.substring(0, alen), b.substring(0, blen-1)));
    }

    /* Given a set of coins. Assume infinite number exists for each
     * denomination. Given a final score, calculate number of ways to summing up
     * the coins to reach the score.
     *
     * Below algo takes O(finalScore * number of coins) space. It can be done in
     * O(finalScore) space, becase, in each iteration of ways[][] array, it only
     * needs previous row and not entire array.
     */
    public int countWays(int []coins, int finalScore) {
        int[][] ways = new int[coins.length][finalScore+1];

        Arrays.sort(coins);

        /* initialize */
        for(int i=0; i<=finalScore; i++) {
            if(i%coins[0]==0)   ways[0][i] = 1;
            else                ways[0][i] = 0;
        }

        for(int i=1; i<coins.length; i++) {
            for(int j=0; j<=finalScore; j++) {
                ways[i][j] = ways[i-1][j];

                for(int k=1; k*coins[i]<=j; k++) {
                    ways[i][j] += ways[i-1][j-k*coins[i]];
                }
            }
        }

        return ways[coins.length-1][finalScore];
    }

    /* C(n, k) = C(n-1, k-1) + C(n-1, k)
     * nth element may be picked - C(n-1, k-1)
     * OR nth element is NOT picked - C(n-1, k)
     */
    public int binomialCoeff(int n, int k) {
        if(n==0)    return 1;
        if(k==0 || k==n)    return 1;

        return binomialCoeff(n-1, k) + binomialCoeff(n-1, k-1);
    }

    /* Given number of bits, return number of numbers with no consecutive 1s
     * Ex: bits = 3; 000, 001, 010, 100, 101 (total 5)
     * */
    public int binString(int bits) {
        int[] count = new int[bits+1];
        Arrays.fill(count, 0);

        count[1] = 2;
        count[2] = 3;

        for(int i=3; i<=bits; i++) {
            count[i] = count[i-1] + count[i-2];
        }

        return count[bits];
    }

    public static void main(String[] a) {
        DP dp = new DP();
        System.out.println(dp.LCS("tree", "ree"));
        System.out.println(dp.lcs.reverse().toString());
    }
}
