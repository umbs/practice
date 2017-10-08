/* Can't exactly recall, but I copied this code from a blog. This isn't my own/original code.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* */
int version(char *v1, char *v2) {
    int *a = malloc(sizeof(int) * strlen(v1));
    int *b = malloc(sizeof(int) * strlen(v2));
    char *tok = NULL;
    int len1, len2;

    /* Parse v1 in to an array */
    tok = strtok(v1, ".");
    for(len1=0; tok; len1++) {
        a[len1] = atoi(tok);
        tok = strtok(NULL, ".");
    }

    /* Parse v2 in to an array */
    tok = strtok(v2, ".");
    for(len2=0; tok; len2++) {
        b[len2] = atoi(tok);
        tok = strtok(NULL, ".");
    }

    for (int i=0; i<len1 || i<len2; i++) {
        if(i<len1 && i<len2) {
            if(a[i] > b[i])         return 1;
            else if(a[i] < b[i])    return -1;
        } else if(i<len1) {
            if(a[i] != 0)           return 1;
        } else if(i<len2) {
            if(b[i] != 0)           return -1;
        }
    }

    return 0;   // versions are same
}

void main() {
    char v1[16];
    char v2[16];
    strcpy(v1, "1.11.0");
    strcpy(v2, "2.1");
    printf("1.11.0 and 2.1 --> %d\n", version(v1, v2));

    strcpy(v1, "1.11.0");
    strcpy(v2, "1.11");
    printf("1.11.0 and 1.11 --> %d\n", version(v1, v2));

    strcpy(v1, "2.1.1");
    strcpy(v2, "2.1.0");
    printf("2.1.1 and 2.1.0 --> %d\n", version(v1, v2));

    strcpy(v1, "2.11.0");
    strcpy(v2, "2.0.1");
    printf("2.11.0 and 2.0.1 --> %d\n", version(v1, v2));
}

