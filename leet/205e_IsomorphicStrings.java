import java.util.*;

public class Solution {
    int[] hs = new int[256];
    int[] ht = new int[256];
    
    public boolean isIsomorphic(String s, String t) {
        if(s==null || t==null)  return false;
        if(s.length() != t.length())    return false;
        
        int len = s.length();
        
        for(int i=0; i<len; i++) {
            char c = s.charAt(i);
            char d = t.charAt(i);
            
            // character mapping must be checked both ways
            if(hs[c]!=0 && hs[c]!=d)    return false;
            if(hs[c]==0 && ht[d]!=0)    return false;
            
            // map characters both ways
            hs[c] = d; ht[d] = c;
        }
        return true;
    }

    public static void main(String[] a) {
        String s = "egg";
        String t = "add"; 
        Solution S = new Solution();
        
        System.out.println(S.isIsomorphic(s, t));
    }
}
