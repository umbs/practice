/*
 * Problems from LeetCode.com
 *
 * P3 - Longest Substring with unique chars
 *
 */
import java.util.*;

public class lss {
    public int lengthOfLongestSubstring(String s) {
        int maxLen=0, st=0, en=0;
        Map<Character, Integer> map = new HashMap<Character, Integer>();

        while (en<s.length()) {
            /* duplicate char in subarray, adjust subarray window and
             * hashmap entries */
            if (map.containsKey(s.charAt(en))) {
                int temp = map.get(s.charAt(en));

                /* drop hashmap entries gone out the window */
                for (int i=st; i<=temp; i++)
                    map.remove(s.charAt(i));

                st = 1+temp;
                continue;
            }

            map.put(s.charAt(en), en);
            en++;
            maxLen = Math.max(maxLen, en-st);
        }

        return maxLen;
    }

    public static void main(String[] args) {
        lss ss = new lss();
        System.out.format("Max substring size: %d\n", ss.lengthOfLongestSubstring("aaaaaa"));
        System.out.format("Max substring size: %d\n", ss.lengthOfLongestSubstring("aab"));
        System.out.format("Max substring size: %d\n", ss.lengthOfLongestSubstring("pwwkew"));
        System.out.format("Max substring size: %d\n", ss.lengthOfLongestSubstring("dvdf"));
    }
}

