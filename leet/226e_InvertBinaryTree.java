/* 226e - Invert a Binary tree
 *
 * 
Following tree:   
     4
   /   \
  2     7
 / \   / \
1   3 6   9

to 

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 * */


public class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root==null)  return root;
        
        TreeNode lnode = root.left;
        TreeNode rnode = root.right;
        
        root.left = rnode;
        root.right = lnode;
        
        invertTree(root.left);
        invertTree(root.right);
        
        return root;
    }
}
