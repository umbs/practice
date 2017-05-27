import java.util.*;

public Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int w1=-1, w2=-1;
        
        for(int i=0; i<len; i++) {
            if(words[i].compareTo(word1)==0)    
                    w1 = i;
            else if(words[i].compareTo(word2)==0)   
                    w2 = i;
            if(w1>-1 && w2>-1)    
                    min = Math.min(min, Math.abs(w1-w2));
        }
                
        return min;
    }
}
