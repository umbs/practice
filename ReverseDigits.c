/*
 * Given a number, return reverse of it's digits
 *
 * -314 --> -413
 *  42 --> 24
 */

#include <stdio.h>
#include <stdlib.h>

int reverseDigits(int in)
{
    int rev = 0, x = in;

    while (x) {
        rev += x%10;    // add last digit to rev
        rev *= 10;      // "decimal left shift"
        x   /= 10;      // "decimal right shift"
    }

    rev /= 10;  // correction for last "left shift"

    if (in < 0)     rev = -rev;

    return rev;
}

int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "./main <number>\n");
        return 0;
    }

    int x = atoi(argv[1]);
    printf("Num after reverse %d \n", reverseDigits(x));

    return 0;
}
