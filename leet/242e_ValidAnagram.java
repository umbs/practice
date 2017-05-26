import java.util.*;

// Assumed ASCII chars so that I can use simple array as hashtable
// Can expand to Unicode or such character set and use Hashtable from Java
// collections. 
public class Solution {
    int[] hs = new int[256];
    int[] ht = new int[256];
    
    public boolean isAnagram(String s, String t) {
      
        // boundary cases
        if(s==null || t==null)  return false;
        if(s.length() != t.length())    return false;
        
        // build hs with counts
        for(int i=0; i<s.length(); i++) {
            hs[s.charAt(i)]++;
        }

        // build ht with counts
        for(int i=0; i<t.length(); i++) {
            ht[t.charAt(i)]++;
        }

        for(int i=0; i<256; i++) {
            if(hs[i] != ht[i])  return false;
        }
        
        return true;
    }
}
