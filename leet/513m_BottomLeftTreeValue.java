/* 513m - Find bottom left tree value 
*/

public class Solution {
    public int value=0, maxLevel=0, level=0;

    public void inOrderWalk(TreeNode n, int level) {
        if(n==null) return;

        /* left most element in a new level */
        if(level > maxLevel) {
            maxLevel = level;
            value = n.val;
        }

        inOrderWalk(n.left, level+1);
        inOrderWalk(n.right, level+1);
    }

    public int findBottomLeftValue(TreeNode root) {
        inOrderWalk(root, level=1);
        return value;
    }
}
