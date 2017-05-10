/* 199m - Right side view of a BT
 *

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

[1, 3, 4]
 
 */
public class Solution {
    
    List<Integer> l = new ArrayList<>();
    public void util(TreeNode node, int level) {
        if(node == null)    return;
        
        if(l.size()==level) l.add(node.val);
        
        util(node.right, level+1);
        util(node.left, level+1);
    }
    public List<Integer> rightSideView(TreeNode root) {
        util(root, 0);
        return l;
    }
}
