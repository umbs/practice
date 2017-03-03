#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

#define MAX_LIST_SZ 100

typedef struct _Node {
    int val;
    struct _Node *next;
} Node;

Node *head;

void printList (Node *head)
{
    printf("List members: ");
    while (head)
    {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}

/* Build a linkedlist of size sz. Members are of type 'int' */
void buildList (Node **head, int sz)
{
    Node *t;

    for (int i=0; i<sz; i++) {
        t = malloc(sizeof(Node));
        t->val = rand()%10;
        t->next = *head;
        *head = t;
    }

    printList(*head);
}

Node *nodeInit(int val)
{
    Node *n = malloc(sizeof(*n));
    n->val = val;
    n->next = NULL;

    return n;
}

Node *addTwoNumbers(Node *l1, Node *l2)
{
    int a, b, carry=0;
    Node *n=NULL, *head=NULL;

    // boundary conditions
    if (l1==NULL && l2==NULL)   return head;

    // special cases
    if (l1==NULL)   return l2;
    if (l2==NULL)   return l1;

    /* 1st node */
    a = l1->val; b = l2->val;
    head = n = nodeInit((a+b+carry)%10);
    carry = (a+b+carry)/10;
    if (l1) l1 = l1->next;
    if (l2) l2 = l2->next;

    /* build the list */
    while(l1 || l2) {
        a = (l1) ? l1->val : 0;
        b = (l2) ? l2->val : 0;

        n->next = nodeInit((a+b+carry)%10);
        n = n->next;
        carry = (a+b+carry)/10;

        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }

    if (carry) {
        n->next = nodeInit(1);
    }

    return head;
}

int main(int c, char *a[])
{
    if (c != 2)  {
        printf("Incorrect args: ./a.exe list-size\n");
        return 1;
    }

    int sz = atoi(a[1]);

    Node *l1=NULL, *l2=NULL, *sum=NULL;

    srand(time(NULL));

    buildList(&l1, sz);
    buildList(&l2, sz);

    sum = addTwoNumbers(l1, l2);
    printList(sum);

    return 1;
}
