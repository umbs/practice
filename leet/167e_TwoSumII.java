public class Solution {
    public int[] twoSum(int[] num, int target) {
        int[] res = new int[2];
        int len = num.length;
        
        for(int i=0, j=len-1; i<j;) {
            int sum = num[i] + num[j];
            
            if(sum==target) {    // found 
                res[0] = i+1; res[1] = j+1;
                return res;
            } 
            else if(sum < target)    
                i++;
            else 
                j--;
        }
        
        return res;
    }
}
