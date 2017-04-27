import java.util.*;

public class Solution {
    /* 492e - Construct a Rectangle such that given an area
     * LxW = area
     * L>=W
     * L-W is minimum
     */
    public int[] constructRectangle(int area) {
        int L=0, W=0;
        
        W = (int)Math.sqrt((double)area);
        L = area/W;
        
        while(L*W != area) {
            W--;
            L = area/W;
        }
        
        System.out.println("L: " + L + ", W: " + W);
        return new int[]{L, W}; 
    }
    public static void main(String[] a) {
        Solution s = new Solution();
        s.constructRectangle(18);
    }
}
