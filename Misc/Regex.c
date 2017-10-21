#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

bool isMatch(const char *t, const char *p);

// p is pointing past the '*' char
bool star(const char cur, const char *t, const char *p) {
    // '*' indicates zero or more chars
    // So, first check for pattern match of string after '*'
    if(isMatch(t, p))
        return true;

    // suffix string (after '*') does not match text
    if(cur==t[0])
        return star(cur, t+1, p);

    return false;
}

/* ? indicates match single char
 * * matches zero or more of previous char
 */
bool isMatch(const char *t, const char *p) {
    if(p[0] == '\0' && t[0] == '\0')
        return true;

    if(p[0] == '\0' || t[0] == '\0')
        return false;

    if(p[0] == '?')
        return isMatch(t+1, p+1);

    // wild card
    if(isalpha(p[0]) && p[1] == '*') {
        return star(p[0], t, p+2);
    }

    if(isalpha(p[0])) {
        return isMatch(t+1, p+1);
    }
}

void main() {
    printf("(abba, ab*?a) %d \n", isMatch("abba", "ab*?a"));
    printf("(abba, a??a) %d \n", isMatch("abba", "a??a"));
}
