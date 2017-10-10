#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "LRUCache.h"
#include "uthash.h"

int main() {
    srand(time(NULL));

    LRUCacheInit(CACHE_SIZE);

    for(int i=0; i<CACHE_SIZE/2; i++) {
        LRUCachePut(cache, rand()%RANGE);
    }

    LRUCachePrint(cache);

    return 0;
}
