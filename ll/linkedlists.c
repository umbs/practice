/* All Geeks for Geeks problems on linked-lists */
/* All reference to 'List' means singly linked list */

#include "linkedlists.h"

#define MAX_LIST_SZ 100

Node *head;
rNode *rhead;

void printList (Node *head)
{
    printf("List members: ");
    while (head)
    {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

/* Print reverse of a linked list using recursion
 * http://www.geeksforgeeks.org/write-a-recursive-function-to-print-reverse-of-a-linked-list/
 * */
void printRevList (Node *head)
{
    if (head == NULL)   return;

    printRevList (head->next);

    printf("%d ", head->data);
}

/* Assume ascending order
 * http://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
 * */
void sortedInsert(Node **head, int data)
{
    Node **cur = head;

    Node *nu = malloc(sizeof(Node));
    nu->data = data;
    nu->next = NULL;

    while (*cur && (*cur)->data < data)
        cur = &((*cur)->next);

    nu->next = *cur;
    *cur = nu;
}

/* Build a linkedlist of size sz. Members are of type 'int' */
void buildList (Node **head, int sz)
{
    //Node *t = NULL;
    int data;

    srand(time(NULL));

    for (int i=0; i<sz; i++) {
        //t = malloc(sizeof(Node));
        //t->data = rand()%100;
        //t->next = *head;
        //*head = t;
        data = rand()%100;
        sortedInsert(head, data);
    }

    printList(*head);
}

/* Assume the list is sorted, remove duplicates from it
 * http://www.geeksforgeeks.org/remove-duplicates-from-a-sorted-linked-list/
 * */
void removeDuplicates (Node **head)
{
    Node **cur = head;

    if (*cur == NULL)   return;

    while (*cur && (*cur)->next) {
        /* duplicate found */
        if ((*cur)->data == (*cur)->next->data) {
            Node *temp = (*cur)->next;
            (*cur)->next = (*cur)->next->next;
            free(temp);
        }

        cur = &((*cur)->next);
    }
}

/* Return size of a list */
uint32_t listSize (Node *head)
{
    uint32_t    sz;

    for (sz=0; head; sz++, head=head->next);

    return sz;
}

/* Build a binary tree (Not a BST)
 * TODO: Incomplete
 */
void buildTree (bNode **head, int nElem)
{
}

/* Get Nth node of the list
 * http://www.geeksforgeeks.org/write-a-function-to-get-nth-node-in-a-linked-list/
 * */
Node *getNth(Node *head, int n)
{
    for (int i=0; i<n-1; i++) {
        if (head==NULL) break;
        head = head->next;
    }

    printf("%d node contains data: %d\n", n, (head)?head->data:INT_MAX);
    return head;
}

/* Delete a node, given it's reference
 * http://www.geeksforgeeks.org/given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/
 * */
void deleteNodeGivenReference(Node **head, Node *del)
{
    Node *this = *head, *that = *head;

    /* 'del' is at start of list */
    if (this == del) {
        *head = (*head)->next;
        free(this);
        goto ret;
    }

    /* 'del' is in middle */
    while (this && this != del) {
        that = this;
        this = this->next;
    }

    /* 'del' not found case */
    if (this == NULL)   goto ret;

    that->next = this->next;
    free(this);

ret:
    printList(*head);
    return;
}

/* Find middle node of a list.
 * TODO: For lists of even size, what is "middle" node? This code gives N/2+1
 * node where N is list size
 *
 *  http://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
 */
Node *findMiddle(Node *head)
{
    Node *mid=head, *end=head->next;

    /* empty and single node lists */
    if (head==NULL || head->next==NULL) goto ret;

    while (end)
    {
        /* mid takes one step, end takes 2 steps */
        mid = mid->next;
        end = end->next;

        if (end)    end = end->next;
        else        break;
    }

ret:
    printf("Data in middle node: %d\n", (mid)?mid->data:INT_MAX);
    return mid;
}

/* Find nth node from end
 * http://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
 * */
Node *findNFromEnd(Node *head, int pos)
{
    Node *this=NULL, *that=head;

    /* walk 1st 'pos' nodes */
    for (int i=0; that && i<pos; i++)    that = that->next;

    /* If list size is < 'pos', return NULL */
    if (that == NULL)   goto ret;

    /* maintain 'pos' distance betwen 'this' and 'that' pointers till end of the
     * list */
    this = head;
    while (that) {
        this = this->next;
        that = that->next;
    }

ret:
    printf("Nth node: %d\n", (this)?this->data:INT_MAX);
    return this;
}

/* Delete the entire list
 * http://www.geeksforgeeks.org/write-a-function-to-delete-a-linked-list/
 * */
void deleteList(Node **head)
{
    Node *t;
    while (*head)
    {
        t = *head;
        *head = (*head)->next;
        free(t);
    }
}

/* Given a key, count it's occurance in the list
 * TODO: Not considering  large list sizes and count overflows
 *
 * http://www.geeksforgeeks.org/write-a-function-that-counts-the-number-of-times-a-given-int-occurs-in-a-linked-list/
 */
int countKey(Node *head, int key)
{
    int count = 0;

    while (head)
    {
        if (head->data == key)  count++;
        head = head->next;
    }

    return count;
}

/* reverse a linked list
 * http://www.geeksforgeeks.org/write-a-function-to-reverse-the-nodes-of-a-linked-list/
 * */
void reverseList(Node **head)
{
    Node *prev=NULL, *cur=NULL, *nxt=NULL;

    if (*head == NULL || (*head)->next == NULL) return;

    cur = *head;    // prev and nxt are NULL

    while (cur->next) {
        nxt = cur->next;    // set nxt pointer
        cur->next = prev;   // link between cur and prev rearranged

        prev = cur; // prev moved by one
        cur = nxt;  // cur moved by one
        nxt = nxt->next;    // nxt moved by one
    }

    cur->next = prev;   // last node settings
    *head = cur;    // Make head ptr point to last node
}

/* Floyd's Cycle finding algo
 * http://www.geeksforgeeks.org/write-a-c-function-to-detect-loop-in-a-linked-list/
 * */
bool findLoop(Node *head)
{
    Node *slow, *fast;

    if (head == NULL || head->next == NULL) return false;

    slow = head; fast = head->next;

    while (slow && fast) {
        slow = slow->next;
        fast = fast->next;

        /* fast moves at twice the rate as slow ptr */
        if (fast && fast->next) fast = fast->next;
        else    return false;   // loop not found

        if (slow == fast)   return true;    // loop found
    }

    return false;
}

/* Check if a list is palindrome
 * Use a stack (array based).
 * - Add elems to it in 1st walk
 * - Compare to the stack in 2nd walk
 *
 * Drawback: Stack size. How big? O(n) extra mem
 *
 * http://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
 */
bool findPalindrome1(Node *head)
{
    Node *walk = head;
    int  st[MAX_LIST_SZ] = {0}, i, list_sz;

    /* build the stack */
    for (i=0; walk && i<MAX_LIST_SZ; i++) {
        st[i] = walk->data;
        walk = walk->next;
    }

    list_sz = i;    // size of the list
    walk = head;

    for (i=list_sz-1; i >= 0 && (st[i]==walk->data); --i) {
        walk = walk->next;
    }

    /* Compared entire list */
    if (i<0)    return true;

    return false;
}

/* - Reverse 2nd half of linked list.
 * - Have two pointers at start and end.
 * - Compare till they meet in middle or mismatch */
bool findPalindrome2(Node *head)
{
    return false;
}

/* Copy contents from src to dst */
void copyNodes(Node *src, Node **dst)
{
    if (src == NULL || dst == NULL)     return;

    if (*dst == NULL)   *dst = malloc(sizeof(Node));
    if (*dst == NULL)   return;     // out of memory

    (*dst)->data = src->data;
    (*dst)->next = src->next;
}

/* Deep copy a linked list */
Node *cloneList(Node *head)
{
    Node *clone=NULL, *walk=NULL;

    if (head == NULL)   return head;

    /* clone points to 1st node */
    clone = walk = malloc(sizeof(Node));
    if (clone == NULL)  return NULL;    // OOM

    while (head) {
        copyNodes(head, &walk);
        walk = walk->next;  // check for OOM
        head = head->next;
    }

    return clone;
}

/* Return a pointer to random node in a list
 * TODO: Make these routines generic (to take Node, rNode or bNode structs
 */
rNode *randNode(rNode *head)
{
    int sz, pos, i;
    rNode *t;

    if (head == NULL)    return NULL;

    /* count size of list */
    for (sz=0, t=head; t; sz++, t=t->next);

    /* generate a random position within the list */
    srand(time(NULL));
    pos = rand()%sz;

    for (i=0, t=head; i<pos; i++) {
        t = t->next;
    }

    return head;
}

/* TODO:
 * build a linked list with nodes containing random and next pointers
 */
void buildRandList(rNode **head, int sz)
{
    rNode *t = NULL;

    srand(time(NULL));
    for (int i=0; i<sz; i++) {
        t = malloc(sizeof(rNode));
        t->data = rand()%100;
        t->next = *head;
        t->rand= randNode(*head);
        *head = t;
    }

    t = *head;

    // print the list
    printf("List members: ");
    while (t) {
        printf("%d %d(rand)", t->data, t->rand->data);
        t = t->next;
    }
}

/* Deep copy a linked list. Nodes contain next and random pointer pointing to
 * any other node in list
 *
 * Solution1: Use a Key-Value pair hash map. Key = address of orig node, Value =
 * address of copy. This takes O(N) memory. I don't know how to implement
 * hashmap in C
 *
 * Solution2: Explained in Method2 at this link
 *  http://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/
 *
 *  Below code is implementation of this
 */
Node *cloneListNextRandom(rNode *head)
{
    return NULL;
}

/* Given two lists that intersect at some point (and remainder is common),
 * return the intersection point/node
 * http://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
 *
 * Implementing 3rd method in above link
 * */
Node *intersectList(Node *head1, Node *head2)
{
    int sz1 = listSize(head1);
    int sz2 = listSize(head2);

    Node *one = head1, *two = head2;

    /* 1st list is bigger */
    if (sz1 > sz2) {
        int diff = sz1-sz2;
        for (int i=0; i<diff; i++)
            one = one->next;
    } else {
        int diff = sz2-sz1;
        for (int i=0; i<diff; i++)
            two = two->next;
    }

    /* one and two are equal length to last node */
    while (one != two) {
        one = one->next;
        two = two->next;
    }

    return one;
}

int main(int c, char *a[])
{
    if (c != 2)  {
        printf("Incorrect args: ./a.exe list-size\n");
        return 1;
    }

    int sz = atoi(a[1]);

    buildList(&head, sz);
    //printRevList(head);

    //getNth(head, 2);
    //deleteNodeGivenReference(&head, getNth(head, 1));
    //findMiddle(head);
    //findNFromEnd(head, 3);
    //deleteList(&head);
    //printf("Count of 6 in list: %d\n", countKey(head, 6));
    //reverseList(&head);
    //findLoop(head); // Need to test
    //printList(cloneList(head));
    //buildRandList(&rhead, c);

    removeDuplicates(&head);
    printList(head);
    return 1;
}
