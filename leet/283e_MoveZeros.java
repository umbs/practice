/* 283e - Move zeroes in an array towards the end of the array 
*/
public class Solution {
    public void moveZeroes(int[] nums) {
        int i, cur;
        for(i=0, cur=0; i<nums.length; i++) {
            if(nums[i]==0) continue;
            nums[cur++] = nums[i];
        }

        while(cur<nums.length)
            nums[cur++] = 0;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {0, 1, 0, 3, 12};
        s.moveZeroes(nums);

        for(int i:nums) {
            System.out.print(i + ", ");
        }
        System.out.println();
    }
}
