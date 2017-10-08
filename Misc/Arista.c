#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <string.h>
#include <sys/time.h>

#define LIST_SZ 10
#define LIST_RANGE 10

// linked list node
typedef struct node_ {
    int data;
    struct node_ *next;
} node;

node *head;

node * newNode(int data) {
    node *n = malloc(sizeof(node));
    n->data = data;
    n->next = NULL;

    return n;
}

// new nodes added to head
void insertNode(node **head, int data) {
    node *n = newNode(data);
    n->next = *head;
    *head = n;
}

void print(node *head) {
    while(head) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

void deleteAllKeys(node **head, int data) {
    node **cur = head;

    while(*cur) {
        if((*cur)->data == data) {
            node *tmp = *cur;
            *cur = (*cur)->next;
            free(tmp);
        } else {
            cur = &((*cur)->next);
        }
    }
}

// if v1 < v2   return -1
// if v1 > v2   return 1
// 0 otherwise
int version(char *v1, char *v2) {
    int a[5] = {0}, b[5] = {0}; // assuming no more than 5 numbers in each version
    int len1, len2;
    char *tok = NULL;

    tok = strtok(v1, ".");
    for(len1=0; tok && len1<5; len1++) {
        a[len1] = atoi(tok);
        tok = strtok(NULL, ".");
    }

    tok = strtok(v2, ".");
    for(len2=0; tok && len2<5; len2++) {
        b[len2] = atoi(tok);
        tok = strtok(NULL, ".");
    }

    int i;
    for(i=0; i<len1 && i<len2; i++) {
        if(a[i] < b[i])     return -1;
        if(a[i] > b[i])     return 1;
    }

    if(i<len1) {
        if(a[i] != 0)   return 1;
    }

    if(i<len2) {
        if(b[i] != 0)   return -1;
    }

    return 0;
}

bool isPal(const char *str) {
    if(str==NULL)   return false;
    int st = 0, en = strlen(str)-1;

    for(;st<en; st++, en--) {
        if(str[st] != str[en])  return false;
    }

    return true;
}

struct s {
    double f;   // 8
    int i;      // 4
    char c[3];  // 3 + 1
    void *p;    // 4
    int x[0];   // 0
};

void main(int argc, char const *argv) {
    for( int i = 0; i < argc; ++i ) {
        printf("%s ", argv[i]);
    }
}
