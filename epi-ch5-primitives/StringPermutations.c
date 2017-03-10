/* All permutations of a string. Bell's algorithm */
#include <stdio.h>
#include <stdlib.h>

void swap(char *a, char *b)
{
    char c = *a;
    *a = *b;
    *b = c;
}

void perm(char *a, int l, int r)
{
    if (l==r) {
        printf("%s\n", a);
        return;
    }

    for (int i=l; i<=r; i++) {
        swap(a+l, a+i);
        perm(a, l+1, r);
        swap(a+l, a+i);
    }
}

int main()
{
    char a[] = "ABC";
    perm(a, 0, 2);
    return 0;
}
