#include <stdio.h>
#include <string.h>

static int min(int a, int b, int c)
{
    if(a>b) a = b;
    if(a>c) a = c;

    return a;
}

/* s, t: two strings; ls, lt: their respective length */
int leven(const char *s, int ls, const char *t, int lt)
{
        int a, b, c;

        /* if either string is empty, difference is inserting all chars
         * from the other
         */
        if (ls<0) return lt;
        if (lt<0) return ls;

        printf("1st string: %d, 2nd string: %d\n", ls, lt);

        /* if last letters are the same, the difference is whatever is
         * required to edit the rest of the strings
         */
        if (s[ls-1] == t[ls-1]) return leven(s, ls - 1, t, lt - 1);

        /* else try:
         *      changing last letter of s to that of t; or
         *      remove last letter of s; or
         *      remove last letter of t,
         * any of which is 1 edit plus editing the rest of the strings
         */
        a = leven(s, ls - 1, t, lt - 1);
        b = leven(s, ls,     t, lt - 1);
        c = leven(s, ls - 1, t, lt    );

        return 1 + min(a, b, c);
}

int main()
{
    char *a = "Kitten", *b = "Sitten";
    printf("Leven Dist: %d\n", leven(a, strlen(a), b, strlen(b)));

    return 0;
}
