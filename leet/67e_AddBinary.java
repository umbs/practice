/* I struggled, again, to implement this. 
 * Solution from here:
 *  https://discuss.leetcode.com/topic/13698/short-ac-solution-in-java-with-explanation/2 
 */

public class Solution {
    public String addBinary(String a, String b) {
        if(a==null || a.isEmpty())  return b;
        if(b==null || b.isEmpty())  return a;

        StringBuilder sb = new StringBuilder();

        int x = a.length()-1, y = b.length()-1, carry = 0, sum = 0;

        while(x>=0 || y>=0 || carry==1) {
            int i = x>=0 ? a.charAt(x)-'0' : 0;
            int j = y>=0 ? b.charAt(y)-'0' : 0;

            sum = (i+j+carry)%2;
            carry = (i+j+carry)/2;

            sb.append(sum);

            x--; y--;
        }

        return sb.reverse().toString();
    }
}
