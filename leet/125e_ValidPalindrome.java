public class Solution {
    public boolean isAlphaNumeric(char c) {
        return Character.isDigit(c) || Character.isLetter(c);
    }
    
    public boolean isPalindrome(String s) {
        if(s.isEmpty()) return true;
        
        for(int i=0, j=s.length()-1; i<j; i++, j--) {
            while(i<j && !isAlphaNumeric(s.charAt(i)))  i++;
            while(i<j && !isAlphaNumeric(s.charAt(j)))  j--;
            
            if(i>j)    return false;
            if(Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j)))  return false;
        }
        
        return true;
    }
}
