/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void inorder(struct TreeNode *node, int *result, int *c, int k) {
    if(node==NULL || *c==k)
        return;

    inorder(node->left, result, c, k);

    (*c)++;
    if(*c==k) {
        *result = node->val;
        return; // no further lookup needed
    }

    inorder(node->right, result, c, k);
}

int kthSmallest(struct TreeNode* root, int k) {
    int result;
    int c = 0;

    inorder(root, &result, &c, k);

    return result;
}
