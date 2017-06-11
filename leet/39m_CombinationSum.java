public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ll = new ArrayList<>();
        Arrays.sort(candidates);
        
        backtrack(ll, new ArrayList<>(), candidates, target, 0);
        
        return ll;
    }
    
    public void backtrack(List<List<Integer>> ll, List<Integer> l, int[] nums, int remain, int start) {
        if(remain < 0)  return;
        if(remain == 0) { ll.add(new ArrayList<>(l)); return; }
        if(start==nums.length)   return;
        
        for(int i=start; i<nums.length && nums[i]<=remain; i++) {
            l.add(nums[i]);
            backtrack(ll, l, nums, remain-nums[i], i);
            l.remove(l.size()-1);
        }
    }
}
