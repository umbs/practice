/* 537m - Multiply two complex numbers
 * (a+bi) x (c+di) = (ac+bd) + (ad+bc)i
 */
import java.util.*;

public class Solution {
    public String complexNumberMultiply(String str1, String str2) {
        String[] str = str1.split("\\+");
        int a = Integer.parseInt(str[0]);
        int b = Integer.parseInt(str[1].substring(0, str[1].length()-1));

        str = str2.split("\\+");
        int c = Integer.parseInt(str[0]);
        int d = Integer.parseInt(str[1].substring(0, str[1].length()-1));

        //System.out.println("a: " + a + ", b: " + b + ", c: " + c + ", " + d);

        int x = a*c-b*d;
        int y = a*d+b*c;

        return Integer.toString(x).concat("+").concat(Integer.toString(y)).concat("i");
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.complexNumberMultiply("1+1i", "1+1i"));
        System.out.println(s.complexNumberMultiply("1+-1i", "1+-1i"));
    }
}
