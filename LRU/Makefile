CC = gcc

all:
	$(CC) --std=c99 -ggdb -c LRUCache.c 
	$(CC) --std=c99 -ggdb -c test.c 
	$(CC) test.o LRUCache.o -o lru
	rm -f LRUCache.o test.o
