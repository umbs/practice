// 1 = Palindrome, 0 = Not
int isPal(const char *s, int lo, int hi) {  // inclusive
    while(lo<=hi) {
        if(s[lo] != s[hi]) {
            return 0;
        }
        lo++; hi--;
    }
    
    return 1;
}

// S(i) = Number of palindrome substrings for string of length i
// S(i) - S(i-1) + X; What is X?
// What is X? Let s be ith character
//      for each s at index j such 0<=j<=i
//          check if char string s_j....s_i is palindrome
int countSubstrings(char* s) {
    int count = 0;
    int len = strlen(s);
    
    for(int i=0; i<len; i++) {
        char c = s[i];
        for(int j=0; j<=i; j++) {
            if(isPal(s, j, i))
                count++;
        }
    }
    
    return count;
}
