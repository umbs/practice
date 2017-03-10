/*
 * Given a number and two bit positions within it, swap the bits.
 */

#include <stdio.h>

long swapBits(long x, int i, int j)
{
    if ((x>>i)&1 == (x>>j)&1)   return x;   // bits are same

    x ^= (1<<i) | (1<<j);   // XOR with 1 flips the bit

    return x;
}

int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "./parity <number>\n");
        return 0;
    }

    long x = atoi(argv[1]);
    printf("Num after swapping 1 & 6 bit %ld --> %ld\n", x, swapBits(x, 1, 6));

    return 0;
}
