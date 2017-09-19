// C program to demonstrate insert operation in binary search tree
// Code is from Geeks for Geeks:
// http://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

#define MAX_Q_CAP 100
#define SZ      15
#define RANGE   45

#define max(x, y)   ((x) > (y) ? (x) : (y))

typedef struct node_ {
    int key;
    struct node_ *left, *right, *parent;
} node;

// A utility function to create a new BST node
node *newNode(int item) {
    node *temp =  (node *)malloc(sizeof(node));
    temp->key = item;
    temp->left = temp->right = temp->parent = NULL;
    return temp;
}

// A utility function to do inorder traversal of BST
void inorder(node *root) {
    if (root == NULL)   return;

    inorder(root->left);
    printf("%d ", root->key);
    //printf("Parent %d\n", root->parent ? root->parent->key : -1);
    inorder(root->right);
}

void preorder(node *root) {
    if (root == NULL)   return;

    printf("Node %d ", root->key);
    printf("Parent %d\n", root->parent ? root->parent->key : -1);
    preorder(root->left);
    preorder(root->right);
}

void postorder(node *root) {
    if (root == NULL)   return;

    postorder(root->left);
    postorder(root->right);
    printf("Node %d ", root->key);
    printf("Parent %d\n", root->parent ? root->parent->key : -1);
}

// Uses quick implementation of queue, without checks on bounds. Not safe, but
// works for PoC/MVP of levelorder printing
void levelorder(node *root) {
    node *que[MAX_Q_CAP];
    int head=0, tail=0; // remove from head and add to tail.

    if(root==NULL)  return;

    que[tail++] = root;
    int size = tail-head;
    int levels = 0;

    while(size && size < MAX_Q_CAP) {
        int len = tail-head;

        printf("Level %d: ", levels);
        for(int i=0; i<len && i<MAX_Q_CAP; i++) {
            node *n = que[head++];

            printf("%d(%d, %d) ", n->key, n->left? n->left->key : -1,
                    n->right?n->right->key : -1);

            if(n->left)  que[tail++] = n->left;
            if(n->right) que[tail++] = n->right;
        }
        printf("\n");
        levels++;

        size = tail-head;
    }
}

// Inorder travel, non-recursive approach
void inorderNR(node *root) {
    if (root == NULL)   return;

    // works like a stack
    node *que[MAX_Q_CAP];
    int top = 0;

    node *n = root;

    while(top != 0 || n != NULL) {
        // push all nodes on to stack
        if(n != NULL) {
            que[top++] = n;
            n = n->left;
        } else {
            n = que[--top];
            printf("%d, ", n->key);
            n = n->right;
        }
    }

    printf("\n");
}

void preorderNR(node *root) {
    if (root == NULL)   return;

    node *que[MAX_Q_CAP];
    int top = 0;
    que[top++] = root;

    while(top) {
        root = que[--top];
        printf("%d ", root->key);

        if(root->right) {
            que[top++] = root->right;
        }

        if(root->left) {
            que[top++] = root->left;
        }
    }
    printf("\n");
}

void postorderNR(node *root) {
    if (root == NULL)   return;

    node *que[MAX_Q_CAP];
    int top = 0;
    que[top++] = root;

    while(top) {
        node *n = que[top-1];
        if(n->left == NULL && n->right == NULL) {
            printf("%d ", n->key);
            top--;
        } else {
            if(n->right) {
                que[top++] = n->right;
                n->right = NULL;
            }

            if(n->left) {
                que[top++] = n->left;
                n->left = NULL;
            }
        }
    }
    printf("\n");
}

// Given an array in inorder form, build a BT (will be BST if array consists of
// ascending numbers)
// Array size is [lo, hi] inclusive
node *inorderToBT(int *arr, int lo, int hi) {
    if(lo > hi) return NULL;

    int mid = lo + (hi-lo)/2;
    node *root  = newNode(arr[mid]);
    root->left  = inorderToBT(arr, lo, mid-1);
    root->right = inorderToBT(arr, mid+1, hi);

    return root;
}

/* A utility function to insert a new node with given key in BST */
node* insert(node* node, int key) {
    /* If the tree is empty, return a new node */
    if (node == NULL) return newNode(key);

    /* Otherwise, recur down the tree */
    if (key < node->key) {
        node->left  = insert(node->left, key);
        node->left->parent = node;
    }
    else if (key >= node->key)  { // duplicates on right side
        node->right = insert(node->right, key);
        node->right->parent = node;
    }

    /* return the (unchanged) node pointer */
    return node;
}

// search for node (first occurance) with 'key'
node *search(node *node, int key) {
    if(node == NULL || node->key==key)  return node;

    // key is smaller than current node
    if(key < node->key)
        return search(node->left, key);

    // key is greater than current node
    return search(node->right, key);
}

node *getRandomNode(node *root) {
    int depth = (int) sqrt(SZ);

    if(root == NULL)    return NULL;

    while(depth) {
        if(root->left == NULL && root->right == NULL)   return root;

        if(root->left == NULL)          root = root->right;
        else if(root->right == NULL)    root = root->left;
        else    root = rand() % 2 ? root->right : root->left;

        depth--;
    }

    return root;
}

void printAncestors(node *node) {
    if(node == NULL)    return;

    while(node) {
        printf("%d -> ", node->key);
        node = node->parent;
    }

    printf("NULL\n");
}

void LCA(node *one, node *two) {
    printAncestors(one);
    printAncestors(two);
}

// Given a node, find it's successor.
// Successor means, when printed in Inorder (ascending), the next key in the
// order
// Two cases determine successor
// 1) If node has right child, it's left most child is successor
// 2) else find an ancestor that is a left child. Return the parent.
node *successor(node *node) {
    if(node==NULL)  return node;

    // (1)
    if(node->right) {
        node = node->right;
        while(node->left)   node = node->left;
        return node;
    }

    // (2)
    while(node->parent && node != node->parent->left)   node = node->parent;

    // Unique case. Node is max node.
    if(node->parent == NULL)    return NULL;

    // at this point, node == node->parent->left
    return node->parent;
}

// Given a node, find it's predecessor.
// Predecessor means, when printed in ascending order, the key before current
// key.
// Two cases determine predecessor
// 1) If node has left child, it's right most child is predecessor
// 2) else find an ancestor that is right child and return the parent
node *predecessor(node *node) {
    if(node==NULL)  return node;

    // (1)
    if(node->left) {
        node = node->left;
        while(node->right)  node = node->right;
        return node;
    }

    // (2)
    while(node->parent && node != node->parent->right)  node = node->parent;

    // Node is smallest in tree
    if(node->parent == NULL)    return NULL;

    // here node == node->parent->right
    return node->parent;
}

// Kth Max key in BST
void getKMaxKey(node *node, int K) {
    // NULL node doesn't mean failure
    if(node == NULL)    return;

    // start from max node and keep finding predecessor
    while(node->right)   node = node->right;

    for(int i=1; i<K; i++) {
        node = predecessor(node);
    }

    printf("%dth largest: %d\n", K, node ? node->key : -1);
}

int longestBranch(node *node, int len) {
    static int depth;

    if(node == NULL)    return 0;

    depth = max(depth, len);

    longestBranch(node->left, len+1);
    longestBranch(node->right, len+1);

    return depth;
}

// Delete first instance of key and return 0 on success or -1 if no node with
// 'key' exists.
// Hibbard Deletion:
int delete(node *node, int key) {
    if(node == NULL)    return -1;  // key not found

    return 0;
}

/* pre-order printing */
void serialize(node *root, int *arr, int *sz) {
    static int idx;

    if(root==NULL)  { arr[idx++] = -1; return; }

    arr[idx++] = root->key;

    serialize(root->left, arr, sz);
    serialize(root->right, arr, sz);

    *sz = idx;
}

/* Input is pre-order printed array. Get a BST */
node *deserialize(int *arr) {
    static int idx;
    if(arr[idx] == -1) { idx++; return NULL; }

    node *n = newNode(arr[idx++]);
    n->left = deserialize(arr);
    n->right = deserialize(arr);
    return n;
}

static char arr[16][64];

void findTreeWidth(node *root, int *min, int *max, int dist) {
    if(root==NULL)  return;

    if(dist < *min) {
        *min = dist;
    } else if(dist > *max) {
        *max = dist;
    }

    findTreeWidth(root->left, min, max, dist-1);
    findTreeWidth(root->right, min, max, dist+1);
}

void verticalHelper(node *root, int level) {

    if(root==NULL)  return;

    char buf[8] = {0};
    snprintf(buf, 8, "%d, ", root->key);
    strcat(arr[level], buf);

    verticalHelper(root->left, level-1);
    verticalHelper(root->right, level+1);
}

void vertical(node *root) {
    int min=0, max=0;

    findTreeWidth(root, &min, &max, 0);

    printf("min: %d, max: %d\n", min, max);

    verticalHelper(root, -min);

    for(int i=0; i<=max-min; i++) {
        printf("%s\n", arr[i]);
    }
}

// Driver Program to test above functions
int main() {
    srand(time(NULL));

    node *root = NULL;
    root = insert(root, rand()%RANGE);

    for (int i=0; i<SZ; i++) {
        insert(root, rand()%RANGE);
    }

    levelorder(root);
    //getKMaxKey(root, 3);
    //printf("Depth: %d\n", longestBranch(root, 0));
    //inorder(root);
    //printf("\n");
    //inorderNR(root);

    //int arr[] = {3, 8, 8, 9, 11, 12, 13, 13, 22, 24, 25, 27, 27, 32, 35, 40};
    //node *root = inorderToBT(arr, 0, 15);
    //levelorder(root);

    //preorderNR(root);
    //postorderNR(root);

    printf("\n\n");

    vertical(root);

    return 0;
}
