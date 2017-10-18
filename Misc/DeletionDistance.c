#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int MIN(int x, int y) {
  return x > y ? y : x;
}

/*
S[0...i]
T[0...j]
DD(S[0...i], T[0...j]) = 1 + DD(S[0...i-1], T[0....j]) (1)
                         1 + DD(S[0...i], T[0...j-1])  (2)
                         DD(S[0...i-1], T[0....j-1])   (3) when S(i) == T(j)

 return MIN(1, 2, 3)
(do, fro)
(d, fr)
1 + ("", fr), 1+(d, f)
*/

/* Improvements:
 * [1]
 * Runtime of solution can be improved by using a 2D array to keep track of
 * subproblems.
 *
 * [2]
 * Another approach is to find length of LCA (Longest Common Subsequence) and
 * subtract it from both the strings.
 * i.e., Deletion Distance = (len1-lenLCA) + (len2-lenLCA)
 * */

int dd(char *str1, int len1, char *str2, int len2) {
  // terminating conditions
  if(len1<0) return len2+1;
  if(len2<0) return len1+1;

//  int three = (str1[len1-1] == str2[len2-1] ? 0 : deletionDistance
  char a = str1[len1];
  char b = str2[len2];


  if(a==b)  {
    return dd(str1, len1-1, str2, len2-1);
  }
  else {
     return 1 + MIN(dd(str1, len1-1, str2, len2), dd(str1, len1, str2, len2-1));
  }
}

int deletionDistance(char *str1, char *str2) {
  return dd(str1, strlen(str1)-1, str2, strlen(str2)-1);
}

int main() {
  printf("(dog, frog): %d\n", deletionDistance("dog", "frog"));
  printf("(, hit): %d\n", deletionDistance("", "hit"));
  printf("(neat, ): %d\n", deletionDistance("neat", ""));
  printf("(neat, hit): %d\n", deletionDistance("neat", "hit"));
  printf("(hot, not): %d\n", deletionDistance("hot", "not"));
  printf("(some, thing): %d\n", deletionDistance("some", "thing"));
  printf("(abc, adbc): %d\n", deletionDistance("abc", "adbc"));
  printf("(awesome, awesome): %d\n", deletionDistance("awesome", "awesome"));
  printf("(ab, ba): %d\n", deletionDistance("ab", "ba"));
  return 0;
}
