// C program to demonstrate insert operation in binary search tree
// Code is from Geeks for Geeks: 
// http://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct node {
    int key;
    struct node *left, *right;
};
  
// A utility function to create a new BST node
struct node *newNode(int item) {
    struct node *temp =  (struct node *)malloc(sizeof(struct node));
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
}
  
// A utility function to do inorder traversal of BST
void inorder(struct node *root) {
    if (root == NULL)   return;

    inorder(root->left);
    printf("%d\n", root->key);
    inorder(root->right);
}

void preorder(struct node *root) {
    if (root == NULL)   return;

    printf("%d\n", root->key);
    preorder(root->left);
    preorder(root->right);
}

void postorder(struct node *root) {
    if (root == NULL)   return;

    postorder(root->left);
    postorder(root->right);
    printf("%d\n", root->key);
}

/* A utility function to insert a new node with given key in BST */
struct node* insert(struct node* node, int key) {
    /* If the tree is empty, return a new node */
    if (node == NULL) return newNode(key);
 
    /* Otherwise, recur down the tree */
    if (key < node->key)
        node->left  = insert(node->left, key);
    else if (key >= node->key)  // duplicates on right side
        node->right = insert(node->right, key);   
 
    /* return the (unchanged) node pointer */
    return node;
}

// search for node (first occurance) with 'key'
struct node *search(struct node *node, int key) {
    if(node == NULL || node->key==key)  return node;

    // key is smaller than current node
    if(key < node->key)
        return search(node->left, key);

    // key is greater than current node
    return search(node->right, key);
}

/* successor 
 * predecessor 
 * getKMaxKey
 * getKMinKey
 * */

// Max key in BST
int getMaxKey(struct node *node) {
    if(node == NULL)            return -1;  // invalid case
    if(node->right == NULL)     return node->key; // max key in BST

    // node has right child
    return getMaxKey(node->right);
}

// Kth Max key in BST
int getKMaxKey(struct node *node, int count, int K) {
    return -1;
}

// 2nd Max key in BST
int get2MaxKey(struct node *node, int nextMax) {
    if(node == NULL)            return -1;  // invalid case
    if(node->right == NULL)     return nextMax; // 2nd max key in BST

    // node has right child
    return get2MaxKey(node->right, node->key);
}

// Min key in BST
int getMinKey(struct node *node) {
    if(node == NULL)           return -1;  // invalid case
    if(node->left == NULL)     return node->key; // min key in BST

    // node has left child
    return getMaxKey(node->left);
}

// Kth Min key in BST
int getKMinKey(struct node *node) {
    return -1; 
}

// Delete first instance of key and return 0 on success or -1 if no node with
// 'key' exists 
int delete(struct node *node, int key) {
    if(node == NULL)    return -1;  // key not found

    return 0;
}

// Driver Program to test above functions
int main() {
#if 0
    /* Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 */
    struct node *root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
#endif

    srand(time(NULL));

    struct node *root = NULL;
    root = insert(root, rand()%100);

    for (int i=0; i<15; i++) {
        insert(root, rand()%45);
    }

    // print inoder traversal of the BST
    inorder(root);

    printf("2nd Max: %d\n", get2MaxKey(root->right, root->key));

    //printf("Searching for 22: %s\n", search(root, 22)==NULL ? "Not Found" : "Found"); 
    
    return 0;
}
