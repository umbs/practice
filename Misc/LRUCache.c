#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define RANGE   50

typedef struct node_ {
    int key;
    struct node_ *prev, *next;
} node;
node *head;

// Use this array as a hash table
// key is index and value is pointer to node in double linked list
node *hash[RANGE];

node *newNode(int key) {
    node *n = malloc(sizeof(node));
    n->key = key;
    n->prev = NULL;
    n->next = NULL;

    return n;
}

// insert at the start
void insert(node **head, int key) {
    node *n = newNode(key);
    n->next = *head;
    if(*head)   (*head)->prev = n;
    *head = n;
}

void print(node *head) {
    while(head) {
        printf("%d ", head->key);
        head = head->next;
    }
    printf("\n");
}

int LRUCachePut() {
}

int LRUCacheGet() {
}

int main() {
    srand(time(NULL));

    for(int i=0; i<15; i++) {
        insert(&head, rand()%RANGE);
    }

    print(head);
    return 0;
}
