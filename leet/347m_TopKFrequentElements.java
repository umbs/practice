import java.util.*;

// Solution from Discussion Forums

// 1) Count frequency of each number and maintain it in Hashtable
// 2) Keep track of max frequency.
// 3) Define an array of lists. Array size is max frequency.
// 4) Bucket sort. Each number will be added to list at it's frequency. Index of array becomes frequency of the number.

public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Hashtable<Integer, Integer> freq = new Hashtable<>();
        int maxFrequency=0;
        
        // walk through the array and count frequency
        for(int i:nums) {
            int count = freq.getOrDefault(i, 0); 
            if(maxFrequency < count+1)    maxFrequency = count+1;
            freq.put(i, count+1);
        }

        for(int key:freq.keySet()) {
            int count = freq.get(key);
            System.out.println("Num: " + key + ", Freq: " + count);
        }        
        
        // bucket sort numbers based on their frequency count
        List<Integer> []bucket = new List[maxFrequency+1];
        
        for(int key : freq.keySet()) {
            int hz = freq.get(key);
            if(bucket[hz] == null)    bucket[hz] = new ArrayList<>();
            bucket[hz].add(key);
        }
        
        List<Integer> res = new ArrayList<>();
        
        // Return only the top K frequently seen numbers
        for(int i=bucket.length-1; i>=0 && res.size()<k; i--) {
            if(bucket[i] != null)  res.addAll(bucket[i]);
        }
        
        return res;
    }
}
