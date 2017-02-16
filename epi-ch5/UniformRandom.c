/* Given a random number generator that produces 0 or 1, return a uniformly
 * random number in the range [a,b] inclusive, where a,b are non-zero numbers,
 * a <= b */

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

#define TRIALS  10000
typedef int (*randFunc)(int, int);

int rand0or1()
{
    return rand()%2;
}

/* My code. The distribution is Bell Curve of sorts. Beginning and end numbers
 * in the range have less likelihood of being selected vs middle numbers */
int uniformRandom1(int a, int b)
{
    int res = a;
    int num = b-a+1;

    for (int i=0; i<num; i++) {
        res += rand0or1();
    }

    return res;
}

/* EPI's solution.
 *
 * This solution too is buggy. It's not "uniform" */
int uniformRandom2(int a, int b)
{
    int res = 0;
    int num = b-a+1;

    for(int i=0; (1<<i) < num; i++) {
        res |= rand0or1();
        res <<= 1;
    }
    res += a;

    return res;
}

/* Very rudimentary test of randomness */
void testRandom(randFunc rF, int a, int b)
{
    if (rF == NULL) return;

    float   *dist;
    dist = malloc(sizeof(float) * (b-a+1));

    int num = b-a+1;
    for (int i=0; i<num; i++) dist[i] = 0.0;

    for (int i=0; i<TRIALS; i++) {
        int res = uniformRandom1(a, b);
        dist[res-a]++;
    }

    /* Each number must have equal distribution */
    for (int i=0; i<num; i++) {
        printf("%d = %f\n", i+a, dist[i]/TRIALS);
    }
}

int main(int argc, char *argv[])
{
    if (argc !=3) {
        printf("Invalid args: ./main a b");
        return 1;
    }

    srand(time(NULL));

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    if (b == a) return 1;

    //printf("Rand between %d and %d: %d\n", a, b, uniformRandom1(a, b));
    ///testRandom(uniformRandom1, a, b);
    testRandom(uniformRandom2, a, b);

    printf("\n");

    return 1;
}
