public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        int[] nums = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9};
        List<List<Integer>> ll = new ArrayList<>();
        boolean[] used = new boolean[10];
        Arrays.fill(used, false);
        
        backtrack(ll, new ArrayList<Integer>(), nums, used, k, n, 0);
        return ll;
    }
    
    public void backtrack(List<List<Integer>> ll, List<Integer> l, int[] nums, boolean[] used, int k, int n, int start) {
        if(k==0 && n==0) {  ll.add(new ArrayList<>(l)); return; }
        if(k<=0 || n<=0)    return;
        if(start >= nums.length)    return;
        
        for(int i=start; i<nums.length && nums[i]<=n; i++) {
            if(used[i]) continue;
            
            used[i] = true;
            l.add(nums[i]);
            backtrack(ll, l, nums, used, k-1, n-nums[i], i+1);
            l.remove(l.size()-1);
            used[i] = false;
        }
    }
}
