public class Solution {
    
    public int oneDigit(int s) {
        return s==0 ? 0 : 1;
    }
    
    public int twoDigits(int s) {
        return (s>0 && s<27) ? 1 : 0;
    }
    
    public int numDecodings(String s) {
        if(s==null || s.isEmpty())  return 0;
      
        int len = s.length();
        
        if(len==1)  return oneDigit(Integer.parseInt(s));
        
        int a = Integer.parseInt(s.substring(0,1));
        int b = Integer.parseInt(s.substring(0,2));
        
        return oneDigit(a) + twoDigits(b) + numDecodings(s.substring(1, len)) + numDecodings(s.substring(2, len));
    }
}
