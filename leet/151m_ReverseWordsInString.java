/* 151m - Reverse words in a string
 * Given a string, reverse the words (last appearing first in result)
 * 
 * Took O(N) extra space by using Stack. Must solve in-place.
 */
import java.util.*;

public class Solution {
    public String reverseWords(String str) {
        str = str.trim();
        if(str.length()<2)  return str;

        StringBuilder rev = new StringBuilder();
        Stack<String> s = new Stack<String>();

        String[] split = str.split(" ", Integer.MAX_VALUE);

        for(String o : split) {
            if(o.length()==0)   continue;
            s.push(o);
        }

        while(s.empty()==false) {
            rev.append(s.pop());
            rev.append(" ");
        }

        return rev.toString().trim();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String str = "Hello World!";
        System.out.println(str +"\n" + s.reverseWords(str));
        str = " ";
        System.out.println(str +"\n" + s.reverseWords(str));
        str = "   a   b ";
        System.out.println(str +"\n" + s.reverseWords(str));
    }
}
