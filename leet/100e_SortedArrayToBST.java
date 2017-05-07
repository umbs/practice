/* 100e - Convert a Sorted Array in to a BST
 */
public class Solution {
    public TreeNode util(int[] nums, int lo, int hi) {
        if(lo>hi)   return null;
        
        int mid = lo + (hi-lo)/2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = util(nums, lo, mid-1);
        node.right = util(nums, mid+1, hi);
        
        return node;
    }
    
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length==0)  return null;
        
        TreeNode head = util(nums, 0, nums.length-1);
        
        return head;
    }
}
