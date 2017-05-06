/* 543e
 *
 * Diameter of a Binary Tree.
 *
 * Diameter = Longest distance between two nodes in the tree.
 *
 * Compute height of a node from bottom of tree (leaf node has zero height).
 * Compute height of left node.
 * Compute height of right node.
 * Compute offset (if left node and right node, both exists, offset is 2. Only
 * one exists, offset is 1)
 *
 * Compute diameter at each node: leftHeight + rightHeigh + offset
 * */

int maxDiameter = 0;

/* max height of a tree rooted at 'node' */
public int heightAtNode(TreeNode node) {
    int offset;
    
    if(node==null)  return 0;
    if(node.left==null && node.right==null) return 0;
    if(node.left==null || node.right==null) offset = 1;
    else offset = 2;
    
    int leftHeight = heightAtNode(node.left);
    int rightHeight = heightAtNode(node.right);
    int diameter = leftHeight + rightHeight + offset;
    
    maxDiameter = Math.max(maxDiameter, diameter);
    
    return 1+Math.max(leftHeight, rightHeight);
}

public int diameterOfBinaryTree(TreeNode root) {
    heightAtNode(root);
    return maxDiameter;
}
