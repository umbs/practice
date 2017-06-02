import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

public class Solution {
    String map[] = new String[] {"", "", "abc", "def", "ghi", "jkl", 
                      "mno", "pqrs", "tuv", "wxyz"};
  
    List<String> result = new ArrayList<>();
    
    public void helper(String digits, StringBuilder sb) {
        if(digits==null || digits.isEmpty()) {
            result.add(sb.toString());
            return;
        }
      
        int len = digits.length();
      
        /// for each digit in input
        int num = digits.charAt(0)-'0';

        // for each alphabet represented by the digit, append it to result
        for(int j=0; j<map[num].length(); j++) {
          helper(digits.substring(1, len), sb.append(map[num].charAt(j)));
          sb.deleteCharAt(sb.length()-1);
        }
    }
  
    public List<String> letterCombinations(String digits) {
        StringBuilder sb = new StringBuilder();
      
        helper(digits, sb);
      
        return result;
    }
  
    public static void main(String[] xyz) {
        Solution S = new Solution();
      
        for(String s : S.letterCombinations("243")) {
            System.out.println(s);
        }
    }
}
