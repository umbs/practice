#include "LRUCache.h"

LRUCache *cache;

static
node *newNode(int key) {
    node *n = malloc(sizeof(node));

    // malloc failed
    if(!n)  return n;

    n->key = key;
    n->prev = NULL;
    n->next = NULL;

    return n;
}

// insert at the start
static
node *insert(node **head, int key) {
    node *n = newNode(key);

    // new node creation failed
    if(!n)  return n;

    n->next = *head;
    if(*head)   (*head)->prev = n;
    *head = n;

    return n;
}

// get first instance of node containing 'key'
static
node *get(LRUCache *cache, int key) {
    KV *hh;
    HASH_FIND_INT(cache->hash, &key, hh);

    if(hh == NULL)  return NULL;

    return hh->n;
}

// first instance of key is removed
static
void delete(node **head, int key) {
    node **cur = head;

    while(*cur && (*cur)->key != key) {
        cur = &((*cur)->next);
    }

    if(*cur == NULL)    return;

    node *tmp = *cur;

    if((*cur)->next) {
        (*cur)->next->prev = (*cur)->prev;
    }
    *cur = (*cur)->next;

    free(tmp);
}

// move node 'n' to head of the list
static
void moveToStart(node **head, node *n) {
    if(n->prev) {
        n->prev->next = n->next;
    }

    if(n->next) {
        n->next->prev = n->prev;
    }

    n->prev = NULL;
    n->next = (*head);
    (*head)->prev = n;

    *head = n;
}

void LRUCacheInit(int size) {
    cache = malloc(sizeof(LRUCache));
    assert(cache != NULL);  // abort if cache init fails

    cache->head = NULL;
    cache->tail = NULL;
    cache->hash = NULL;
    cache->size = size;
}

void LRUCachePrint(LRUCache *cache) {
    node *head = cache->head;
    while(head) {
        printf("%d ", head->key);
        head = head->next;
    }
    printf("\n");
}

// If key exists, bring it to front of list (equivalent to updating timestamp on
// a cache entry)
// If key doesn't exist, check if cache is full:
//      if full
//          evict last element 
//      add element at start
int LRUCachePut(LRUCache *cache, int key) {
    assert(cache != NULL);
    node *head = cache->head;

    //[1] if key exists nothing to do (or should be it be moved to front of the
    //list?)
    if(get(cache, key) != NULL) {
        return SUCCESS;
    }

    // cache full. Eviction! Last node in LRU
    if(cache->size == CACHE_SIZE) {
        // get the tail ptr and correct it
        node *tmp = cache->tail;
        cache->tail = cache->tail->prev;

        KV *del;
        HASH_FIND_INT(cache->hash, &tmp->key, del);
        if(del) {
            HASH_DEL(cache->hash, del); 
        }
        free(tmp);
        cache->size--;
        /* end - last node removed */
    }

    // add element at start

    // insert in to double LL
    node *n = insert(&cache->head, key);
    // add to hash table
    KV *hh = malloc(sizeof(KV));
    hh->key = key;
    hh->n   = n;
    HASH_ADD_INT(cache->hash, key, hh);

    cache->size++;
}

int LRUCacheGet() {
}
