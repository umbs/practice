"""
2/23/20 - Mock interview on InterviewBit

Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

Note:
1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1

2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2

Example:
Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)


If no solution is possible, return an empty list.




1st solution - Brute Force: i, j, k, l - O(N^4)

2nd solution -
  * for each pair (i, j) in array A, put in dict with A[i] + A[j], (i, j)
  * for each pair (k, l) in array A - O(N^2)
      - look for (i, j) such that A[k] + A[l] == A[i] + A[j]

[0,1], [0,2], [0,3] ....
[1,2], [1,3], ....
[2,3], [2,4], ....

[0, 2] = 10. 10 is not in dict
[3, 5] look for 10 in dict, [0, 2] = [0, 2, 3, 5]
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        d = dict()

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                s = A[i] + A[j]
                # key = s, Value = [(0,2), (3,5), (4,6)]
                val = d.get(s, list())
                val.append((i, j))
                d[s] = val

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                s = A[i] + A[j]
                if s in d:
                    val = d.get(s)
                    for k, l in val:
                        if k != i and k != j and l != i and l != j:
                            return [i, j, k, l]

        return []


if __name__ == "__main__":
    s = Solution()
    print(s.equal([1, 1, 1, 1, 1]))
    print(s.equal([3, 4, 7, 1, 2, 9, 8]))
