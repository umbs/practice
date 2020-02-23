"""
2/23/20 - Mock interview on InterviewBit

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
