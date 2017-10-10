#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

#include "uthash.h"

#define RANGE 20
#define CACHE_SIZE  15

#define SUCCESS 0
#define ERROR -1

// node in doubly linked list
typedef struct node_ {
    int key;
    struct node_ *prev, *next;
} node;

// key-value pair for hash table
typedef struct KV_ {
    int key;            // same as key in doubly LL
    node *n;            // node of doubly LL in which 'key' is present
    UT_hash_handle hh;    
} KV;

typedef struct LRUCache_ {
    node    *head;
    node    *tail;
    KV      *hash;
    int     size;
    int     capacity;
} LRUCache;

extern LRUCache *cache;

void LRUCacheInit(int size);
void LRUCachePrint(LRUCache *cache);
int LRUCachePut();
int LRUCacheGet();
