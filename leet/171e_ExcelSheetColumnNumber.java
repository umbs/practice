import java.util.*;

// Similar to converting a number in base 26 system to decimal system

public class Solution {
    public int titleToNumber(String s) {
        if(s.length()==0)    return 0; // not sure
        
        String l = s.toLowerCase();
        int res = 0; 
        
        for(int i=0; i<l.length(); i++) {
            res *= 26;
            res += l.charAt(i)-96;
        }
        
        return res;
    }
}
