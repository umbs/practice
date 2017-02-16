/* Given a number (64-bit or any long number), find it's Parity.
 * 1 if odd number of bits set
 * 0 otherwise
 *
 * 13 = 0000 1101 = Parity is 1
 * 17 = 0001 0001 = 0
 */

#include <stdio.h>

short parity(long x)
{
    short r = 0;
    while (x) {
        r ^= 1;
        x &= (x-1); // clears last set bit
    }

    return r;
}

int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "./parity <number>\n");
        return 0;
    }

    long x = atoi(argv[1]);
    printf("Parity of %ld: %d\n", x, parity(x));

    return 0;
}
