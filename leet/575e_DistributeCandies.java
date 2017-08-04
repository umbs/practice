public class Solution {
    public int distributeCandies(int[] candies) {
        Arrays.sort(candies);
        int count = 1;
        
        for(int i=1; i<candies.length; i++)
            if(candies[i-1] != candies[i])  
                count++;
        
        return Math.min(count, candies.length/2);
    }
}
