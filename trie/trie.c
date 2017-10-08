
#define ALPHABET 26

typedef struct trie_s {
    char c;
    struct trie_s *next[ALPHABET];
} trie;

trie *newTrie(char c) {
    trie *t = malloc(sizeof(trie));
    t->c = c;
    
    for(int i=0; i<ALPHABET; i++) {
        t->next[i] = NULL;
    }

    return t;
}

trie *root = newTrie('.');

void addNode(trie *root, char c) {
    if(root==NULL)  return;

    int idx = c-'a';

    if(root->next[idx] == NULL) {
        root->next[idx] = newTrie(c);
    }
}

void insert(trie *root, char *str) {
}
