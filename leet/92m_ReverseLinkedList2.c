#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *head;

void printList(struct ListNode *head) {
    printf("List members: ");
    while(head) {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}

/* Build a linkedlist of size sz. Members are of type 'int' */
void buildList (struct ListNode **head, int sz) {
    struct ListNode *t = NULL;
    //int data;

    srand(time(NULL));

    for (int i=0; i<sz; i++) {
        t = malloc(sizeof(struct ListNode));
        t->val = rand()%100;
        t->next = *head;
        *head = t;
    }

    printList(*head);
}

struct ListNode* reverseBetween(struct ListNode* head, int m, int n) {
    struct ListNode *prev=NULL, *cur=NULL, *nxt=NULL;

    if(head==NULL)  return head;
    if(m>=n)    return head;

    cur = head;

    // Go to m'th node
    for(int i=1; i<m; i++) {
        nxt = cur->next;    // setup nxt
        prev = cur;         // setup prev
        cur = cur->next;

        // list is not big enough
        if(cur==NULL)   return head;
    }
    if(cur) nxt = cur->next;
    else    nxt = NULL;
    
    struct ListNode *beg, *end;
    beg = prev;

    // setup prev, cur, nxt pointers
    prev = cur;
    cur = cur->next;

    // reverse n-m+1 nodes
    for(int i=1; i<(n-m+1); i++) {
        nxt = cur->next;     
        cur->next = prev;

        prev = cur;
        cur = nxt;
    }
    end = cur->next;

    printf("\n");

    printf("Beg: %d, End: %d\n", beg->val, end->val);
}

int main() {
    buildList(&head, 20);
    reverseBetween(head, 3, 5);
    return 1;
}
