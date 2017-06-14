public class Solution {
    public String convertToTitle(int n) {
        String[] alph = new String[] {"Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"};
        
        int rem=0;
        StringBuilder res = new StringBuilder();
        
        while(n>0) {
            rem = n%26;
            n /= 26;
            
            if(rem==0)  n--;
            
            res.append(alph[rem]);
        }
        
        return res.reverse().toString();
    }
}
