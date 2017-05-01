/* 547m - Friend Circles 
 * Similar to Union/Find problem (or Connected Components problem) 
 * */

import java.util.*;

public class Solution {
    public int cirCount;

    public void addToCircle(int[] friends, int i, int j) {
        int old, nu;
        
        if(friends[i]<friends[j])   { old = friends[j]; nu = friends[i]; }
        else                        { old = friends[i]; nu = friends[j]; }
        
        for(int k=0; k<friends.length; k++) {
            if(friends[k] == old)   friends[k] = nu;
        }
    }
    
    public int findCircleNum(int[][] M) {
        int sz = M[0].length;
        int friends[] = new int[sz];
        cirCount = sz;  // at most each friend is in their own circle
        
        // initialize
        for(int i=0; i<friends.length; i++) {
            friends[i] = i;
        }
    
        for(int i=0; i<sz; i++) {
            for(int j=i+1; j<sz; j++) {
                if(M[i][j]==1 && friends[i] != friends[j]) {
                    addToCircle(friends, i, j);
                    cirCount--;
                }
            }
        }
        
        return cirCount;
    }

    public static void main(String[] a) {
        Solution s = new Solution();
        int[][] M1 = {{1,0,0,1}, {0,1,1,0}, {0,1,1,1}, {1,0,1,1}};
        int[][] M2 = {{1,1,0},{1,1,0},{0,0,1}};
        int[][] M3 = {{1,1,0},{1,1,1},{0,1,1}};
        
        System.out.println("M1: " + s.findCircleNum(M1));
        System.out.println("M2: " + s.findCircleNum(M2));
        System.out.println("M3: " + s.findCircleNum(M3));
    }
}
