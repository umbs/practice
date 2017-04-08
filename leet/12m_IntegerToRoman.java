/*
 * 12m Convert an Integer to Roman
 *
 * The input is guaranteed to be between 1 and 3999
 *
 */
public class Solution {
    public final int deno[] = { 1,   4,    5,   9,    10,   40,    50,   90,  100,  400,  500, 900, 1000};
    public String sym[] =     {"I", "IV", "V", "IX", "X",   "XL",  "L", "XC", "C", "CD",  "D", "CM", "M"};

    public String intToRoman(int num) {
        String res="";
        int fac;

        for(int i=sym.length-1; i>=0; i--) {
            fac = num/deno[i];

            if(fac==0)  continue;
            while(fac-->0)  res += sym[i];
            num = num%deno[i];
        }

        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println("1: " + s.intToRoman(1));
        System.out.println("16: " + s.intToRoman(16));
        System.out.println("58: " + s.intToRoman(58));
        System.out.println("59: " + s.intToRoman(59));
        System.out.println("190: " + s.intToRoman(190));
    }
}

