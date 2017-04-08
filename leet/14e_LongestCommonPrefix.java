/* 14e Longest Common Prefix
 * Given an array of strings, return longest common prefix. I think a Trie is
 * typically used. But some simple calculations are used here.
 */
public class Solution {
    public int prefixMatch(String one, String two, int endIdx) {
        int i = endIdx;
        while(i>0 && one.substring(0, i).compareTo(two.substring(0, i)) != 0) {
            i--;
        }

        return i;
    }

    public String longestCommonPrefix(String[] strs) {
        if(strs.length==0)  return "";
        if(strs.length==1)  return strs[0];

        int len=strs[0].length();
        int idx=0;

        for(int i=0; i<strs.length; i++) {
            if(len > strs[i].length()) {
                len = strs[i].length();
                idx = i;
            }
        }

        String piv = strs[idx];
        int endIdx = piv.length();

        for(int i=0; i<strs.length; i++) {
            if(i==idx)  continue;
            endIdx = prefixMatch(piv, strs[i], endIdx);
        }

        return piv.substring(0, endIdx);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String[] strs = {"ca", "a"};
        System.out.println(s.longestCommonPrefix(strs));
        String[] strs1 = {"aa", "a"};
        System.out.println(s.longestCommonPrefix(strs1));
    }
}
