/* All Geeks for Geeks problems on linked-lists */

#include "linkedlists.h"

Node *head;

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

/* Build a linkedlist of size sz. Members are of type 'int' */
void buildList (Node **head, int sz)
{
    Node *t = NULL;

    srand(time(NULL));
    for (int i=0; i<sz; i++) {
        t = malloc(sizeof(Node));
        t->data = rand()%100;   // nums are < 100
        t->next = *head;
        *head = t;
    }

    printList(*head);
}

/* Get Nth node of the list */
Node *getNth(Node *head, int n)
{
    for (int i=0; i<n-1; i++) {
        if (head==NULL) break;
        head = head->next;
    }

    printf("%d node contains data: %d\n", n, (head)?head->data:INT_MAX);
    return head;
}

/* Delete a node, given it's reference */
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

/* Find nth node from end */
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

/* Delete the entire list */
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

int main()
{
    buildList(&head, 20);

    //getNth(head, 2);
    //deleteNodeGivenReference(&head, getNth(head, 1));
    //findMiddle(head);
    //findNFromEnd(head, 3);
    //deleteList(&head);
    //printf("Count of 6 in list: %d\n", countKey(head, 6));
}
