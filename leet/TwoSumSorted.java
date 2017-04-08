/* 2Sum on a sorted array
 *
 * Finding 2 numbers in a sorted array that add up to a value of K
 * Sorting takes O(N log N). But finding the pair itself takes O(N) in
 * sorted array.
 */
import java.util.*;

class match {
    int x, y;

    match(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class TwoSumSorted {
    public List<match> twoSum(int[] nums, int K) {
        List<match> l = new ArrayList<match>();

        for(int i=0, j=nums.length-1; i<j;) {
            int sum = nums[i]+nums[j];

            if(sum<K)       i++;
            else if(sum>K)  j--;
            else {
                match m = new match(nums[i], nums[j]);
                l.add(m);
                i++; j--;
            }
        }

        return l;
    }

    public static void main(String[] args) {
        TwoSumSorted s = new TwoSumSorted();
        int[] nums = new int[30];
        Random r = new Random();
        List<match> res;

        for(int i=0; i<nums.length; i++) {
            nums[i] = r.nextInt(31)-15;    // random nums between (-15, 15]
        }

        Arrays.sort(nums);
        for(int i: nums) {
            System.out.print(i + " ");
        }
        System.out.println();

        res = s.twoSum(nums, 0);

        for(match m: res) {
            System.out.println(m.x + "," + m.y);
        }
    }
}
