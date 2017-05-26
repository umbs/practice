import java.util.*;

public class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> m = new Hashtable<>();
        int len = nums.length;
        int res = 0;
        
        for(int i:nums) {
            m.put(i, m.getOrDefault(i, 0)+1);
        }
        
        for(int key : m.keySet()) {
            int count = m.get(key);
            if(count > len/2)  {
                res = key;
                break;
            }
        }
        
        return res;
    }
}
