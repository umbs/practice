int **dp;   // global 2D array

int MAX(int x, int y) {
    return x > y ? x : y;
}

int helper(char *s, int l, int r) {
    if(dp[l][r] != -1) {
        return dp[l][r];
    }

    if(l>r)     return 0;
    if(l==r)    return 1;

    if(s[l]==s[r]) {
        dp[l][r] =  2 + helper(s, l+1, r-1);
    } else {
        dp[l][r] = MAX(helper(s, l+1, r), helper(s, l, r-1));
    }

    return dp[l][r];
}

int longestPalindromeSubseq(char* s) {
    int len = strlen(s);

    // global 2D array
    dp = malloc(len * sizeof(int *));
    for(int i=0; i<len; i++) {
        dp[i] = malloc(len * sizeof(int));
    }

    // Initialize to -1
    for(int i=0; i<len; i++) {
        for(int j=0; j<len; j++) {
            dp[i][j] = -1;
        }
    }

    return helper(s, 0, len-1);
}

/* Solution from Discussion Forum */
