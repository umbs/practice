/*
 * Two strings are given, find smaller one (s) as a subsequence in other (t)
 * Runtime: O(M+N) where M and N are strings lengths of s and t
 */
bool isSubsequence(char* s, char* t) {
    while(*s && *t) {
        if(*s == *t)    s++;
        t++;
    }

    if(*s)  return false;

    return true;
}
