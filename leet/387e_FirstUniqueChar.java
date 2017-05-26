import java.util.*;

// Walk the String and compute count of each char in a hash table
// In 2nd walk of String, first char with '1', return it's index.

public class Solution {
    int ch[] = new int[256]; // init to 0's by default
    public int firstUniqChar(String s) {
        // frequency count
        for(int i=0; i<s.length(); i++) {
            ch[s.charAt(i)]++;
        }
        
        for(int i=0; i<s.length(); i++) {
            if(ch[s.charAt(i)]==1)  return i;
        }
        
        return -1;
    }
}
