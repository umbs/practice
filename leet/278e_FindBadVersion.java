/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int helper(int lo, int hi) {
        if(lo == hi)  return hi;
        if(lo > hi) return hi;
      
        int mid = lo + (hi-lo)/2;
      
        // found an instance of bad version
        if(isBadVersion(mid)) {
            // earlier version could be bad
            if(mid>1 && isBadVersion(mid-1)) {
                // binary search for first version
                return helper(lo, mid-1);
            } else {
                // found the first version
                return mid;
            }
        } else {
            // search in right half for first bad version
            return helper(mid+1, hi);
        }
    }
  
    public int firstBadVersion(int n) {
        if(n==0 || n==1)  return n;
      
        return helper(1, n);
    }
}
