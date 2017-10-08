#include <stdio.h>

int MAX(int x, int y) {
    return x > y ? x : y;
}

/**
 * @input A : String termination by ' * 
 * @Output Integer
 */
int longestValidParentheses(char* A) {
    #define OPEN '('
    #define CLOSE ')'
    
    int open = 0;   // number of open braces so far
    int gmax = 0, lmax;   // global and local max

    for(int i=0; A[i] != '\''; i++) {
        char c = A[i];
        if(c == OPEN) {
            open++;
        } else {
            if(open > 0) {
                open--;
                lmax += 2;
            } else {
                gmax = MAX(gmax, lmax);
            }
        }
    }

    return gmax;
}

int main() {
    char *A = "(()'";
    printf("%d\n", longestValidParentheses(A));
}
