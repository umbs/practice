public class Solution {
    public boolean wordMatch(String row, String pattern) {
        for(int i=0; i<pattern.length(); i++) {
            if(row.indexOf(pattern.charAt(i)) == -1) {
                // System.out.println("Word NOT found: " + pattern);
                return false;
            }
        }
        
        // System.out.println("Word found: " + pattern);
        return true;
    }
    
    public String[] findWords(String[] words) {
        String top = "QWERTYUIOP";
        String mid = "ASDFGHJKL";
        String bot = "ZXCVBNM";

        List<String> res = new ArrayList<>();
        
        for(int i=0; i<words.length; i++) {
            if(wordMatch(top, words[i].toUpperCase()) || 
               wordMatch(mid, words[i].toUpperCase()) || 
               wordMatch(bot, words[i].toUpperCase())) {
                res.add(words[i]);
            }
        }
        
        String[] arr = res.toArray(new String[0]);
        
        return arr;
    }
}
