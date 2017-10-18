#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ASCII_SIZE 255

int MAX(int x, int y) {
    return x > y ? x : y;
}

void clear(char *a, int size) {
    memset(a, size, 0);
}

int longestSubStringWORepeatChars(char *s) {
    char alphabet[ASCII_SIZE] = {0};

    int len = strlen(s);
    int maxLen = 0;
    int start=0, end;

    for(int i=0; i<len; i++) {
        // first occurance of this char
        if(alphabet[s[i]-'a'] == 0) {
            alphabet[s[i]-'a']++;
            end = i;
        } else {    // found a repeating char
            maxLen = MAX(maxLen, end-start+1);
            clear(alphabet, ASCII_SIZE);
            start = i;
        }
    }

    return maxLen;
}

void main() {
    printf(": %d\n", longestSubStringWORepeatChars("hello world"));
}
