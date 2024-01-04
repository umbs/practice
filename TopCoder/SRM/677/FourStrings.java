/* SRM 677 Div 2, Lev 2.
 *
 * I copied (partially) the top submission in Java for this problem. The
 * "brute force" permutations of all 4 strings are from that submission.
 * Rest of string parsing algo is mine.
 */
public class FourStrings {

	public static String superString(String a, String b) {
		int i=0, aLen = a.length();
		int j=0, bLen = b.length();

		if (aLen == 0) return b;
		if (bLen == 0) return a;

		while(i<aLen) {
			while(j<bLen) {
				if (a.charAt(i) == b.charAt(j)) {
					i++; j++;

					/* end of string a */
					if (i==aLen) return a.concat(b.substring(j));

					/* end of string b */
					if (j==bLen) return a;
				} else {
					/* mismatch, right shift b by 1 (brute force search) */
					i = i-j+1;
					j = 0;

					/* end of string a */
					if (i==aLen) return a.concat(b);
				}
			}
		}

		return a.concat(b); /* will never reach here */
	}

	public static int shortestLength(String a, String b, String c, String d) {
		int res = Integer.MAX_VALUE;

	    res = Math.min(res, superString(superString(superString(a, b), c), d).length());
	    res = Math.min(res, superString(superString(superString(a, b), d), c).length());
	    res = Math.min(res, superString(superString(superString(a, c), b), d).length());
	    res = Math.min(res, superString(superString(superString(a, c), d), b).length());
	    res = Math.min(res, superString(superString(superString(a, d), b), c).length());
	    res = Math.min(res, superString(superString(superString(a, d), c), b).length());
	    res = Math.min(res, superString(superString(superString(b, a), c), d).length());
	    res = Math.min(res, superString(superString(superString(b, a), d), c).length());
	    res = Math.min(res, superString(superString(superString(b, c), a), d).length());
	    res = Math.min(res, superString(superString(superString(b, c), d), a).length());
	    res = Math.min(res, superString(superString(superString(b, d), a), c).length());
	    res = Math.min(res, superString(superString(superString(b, d), c), a).length());
	    res = Math.min(res, superString(superString(superString(c, a), b), d).length());
	    res = Math.min(res, superString(superString(superString(c, a), d), b).length());
	    res = Math.min(res, superString(superString(superString(c, b), a), d).length());
	    res = Math.min(res, superString(superString(superString(c, b), d), a).length());
	    res = Math.min(res, superString(superString(superString(c, d), a), b).length());
	    res = Math.min(res, superString(superString(superString(c, d), b), a).length());
	    res = Math.min(res, superString(superString(superString(d, a), b), c).length());
	    res = Math.min(res, superString(superString(superString(d, a), c), b).length());
	    res = Math.min(res, superString(superString(superString(d, b), a), c).length());
	    res = Math.min(res, superString(superString(superString(d, b), c), a).length());
	    res = Math.min(res, superString(superString(superString(d, c), a), b).length());
	    res = Math.min(res, superString(superString(superString(d, c), b), a).length());

		return res;
	}

	/*
	public static void main(String[] a) {
		System.out.println("" + shortestLength(	"abbabadbd", "bsddsbdsd", "bas", "d"));
	}*/
}
