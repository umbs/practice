#include <stdbool.h>
#include <stdio.h>

// if one is true, it's player1's turn
//[1, 5, 2]

//[5, 2]  p1-> 1; p2-> 
//[2]     p1-> 1; p2-> 5
//[]      p1-> 1,2; p2-> 5

bool helper(int *nums, int lo, int hi, int *score1, int *score2, bool one) {
    if(lo>hi) {
        return *score1 > *score2;
    }
    
    int left = nums[lo];
    int rite = nums[hi];

    if(one) {
        *score1 += left;
        bool lresult = helper(nums, lo+1, hi, score1, score2, !one);
        *score1 -= left;
        
        if(lresult)     return true;
        
        *score1 += rite;
        bool rresult = helper(nums, lo, hi-1, score1, score2, !one);
        *score1 -= rite;
        
        return rresult;
        
    } else {
        *score2 += left;
        helper(nums, lo+1, hi, score1, score2, !one);
        *score2 -= left;
        
        *score2 += rite;
        helper(nums, lo, hi-1, score1, score2, !one);
        *score2 -= rite;        
    }
}

bool PredictTheWinner(int* nums, int numsSize) {
    int score1=0, score2=0;
    return helper(nums, 0, numsSize-1, &score1, &score2, true);
}

void main() {
    int nums[] = {1, 5, 2}; 
    printf("Winner: %d\n", PredictTheWinner(nums, 3));
}
