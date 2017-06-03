/* Solution from discussion forum.
 * Key insight is this:
 * If there are K (<=N) numbers whose bits are set at position i then
 * there are (N-K) numbers with 0 in i'th position. Contribution of all those
 * numbers towards total hamming distance is K*(N-K)
 *
 * Now repeat this count for all 32 bits 
 * */



public class Solution {
    public int totalHammingDistance(int[] nums) {
        int total=0, len = nums.length;
        
        for(int i=0; i<32; i++) {
            int bitCount = 0;
            for(int j=0; j<len; j++)
                bitCount += (nums[j]>>i) & 1;
            total += bitCount * (len-bitCount);
        }
        
        return total;
    }
}
