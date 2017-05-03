/**
 * 515m - Find largest number in each level of a binary tree.
 *
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    List<Integer> large = new ArrayList<Integer>();

    public void largestValuesUtil(TreeNode node, int level) {
        if(node==null)  return;

        if(large.size() <= level) {
            large.add(level, new Integer(node.val));
        } else {
            int val = large.get(level).intValue();
            if(node.val > val)  large.set(level, new Integer(node.val));
        }

        largestValuesUtil(node.left, level+1);
        largestValuesUtil(node.right, level+1);
    }

    public List<Integer> largestValues(TreeNode root) {
        largestValuesUtil(root, 0);

        return large;
    }
}
