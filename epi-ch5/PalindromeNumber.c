/* Check if a given number is Palindrome */

#include <stdio.h>
#include <stdbool.h>
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


/* Use solution from ReverseDigits and compare the numbers.
 *
 * The solution involving comparing MSD and LSD seems tedious
 */
bool isPalindromeNumber(int in)
{
    if (in < 0)     return false;
    if (in == 0)    return true;

    return (in == reverseDigits(in));
}

int main(int argc, char *argv[])
{
    if (argc !=2) {
        printf("Invalid args: ./main number");
        return 1;
    }

    int in = atoi(argv[1]);
    printf("%d is Palindrome: %s", in,
            isPalindromeNumber(in)?"True":"False");

    return 1;
}
