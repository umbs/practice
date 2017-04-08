/* 15m - 3Sum adding to zero
 */
import java.util.*;

public class Solution {

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ll = new LinkedList<>();
        List<Integer> l;

        Arrays.sort(nums);  //O(N log N)

        for(int i=0; i<nums.length-1;i++) {
            int a=nums[i];

            // skip duplicates
            if(i>0 && nums[i]==nums[i-1]) continue;

            // 2SUM problem
            for(int j=i+1, k=nums.length-1; j<k && j<nums.length-1;) {

                int sum = nums[j]+nums[k];

                if(sum<-a)       j++;
                else if(sum>-a)  k--;
                else {  // found a triplet
                    ll.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++; k--;

                    // skip duplicates
                    while(j<k && nums[j]==nums[j-1]) j++;
                    while(j<k && nums[k]==nums[k+1]) k--;
                }
            }
        }

        return ll;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = new int[15];
        Random r = new Random();
        List<List<Integer>> res;
        long start, end;

        for(int i=0; i<nums.length; i++) {
            nums[i] = r.nextInt(31)-15;    // random nums between (-15, 15]
        }

        Arrays.sort(nums);
        for(int i: nums) {
            System.out.print(i + " ");
        }
        System.out.println();

        start = System.nanoTime();
        res = s.threeSum(nums);
        end = System.nanoTime();

        for(List l: res) {
            Iterator i = l.iterator();
            while(i.hasNext()) {
                System.out.println(i.next() + "," + i.next() + "," + i.next());
            }
        }

        System.out.println("Duration: " + (long)(end-start)/1000 + "us");
    }
}
