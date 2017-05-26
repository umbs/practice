import java.util.*;

public class Solution {
    
    int[] orig;
    int[] shuf;
    
    public Solution(int[] nums) {
        orig = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return orig;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        // Using Knuth Shuffle algo
        // In iteration i, choose a random number r between 0 and i-1
        // replace i'th element with r'th element
        int len = orig.length;
        int[] shuf = new int[len];
        shuf = Arrays.copyOf(orig, len);
        Random r = new Random();
 
        for(int i=1; i<len; i++) {
            int j = r.nextInt(i);
            // swap j and i elements 
            int tmp = shuf[j];
            shuf[j] = shuf[i];
            shuf[i] = tmp;
        }
        
        return shuf;
    }  
}
