import java.util.*;

public class DP {

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

    public static void main(String[] a) {
        DP dp = new DP();
        System.out.println(dp.LCS("tree", "ree"));
        System.out.println(dp.lcs.reverse().toString());
    }
}
