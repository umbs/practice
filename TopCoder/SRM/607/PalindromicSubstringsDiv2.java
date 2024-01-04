
public class PalindromicSubstringsDiv2 {

	static boolean isPal(String s) {
		for(int i=0, len=s.length(); i<len/2; i++) 
			if(s.charAt(i) != s.charAt(len-i-1)) 
				return false; 
		
		return true; 
	}
	
	static String cc(String[] s) {
		StringBuilder b = new StringBuilder(); 
		
		for(String sub : s)
			if(sub.compareTo("") != 0)
				b.append(sub);
		
		return b.toString(); 
	}
	
	public static String[] subStrArr(String s) {
		int len = s.length(); 
		int idx = 0; 
		String[] sub = new String [len * (len+1)/2]; 
				
		for(int sz=1; sz<=len; sz++) {
			for(int i=0; i+sz<=len; i++) {
				sub[idx] = s.substring(i, i+sz);
				idx++; 
			}
		}
		
		return sub; 
	}
	
	public static int count(String[] S1, String[] S2) {
		int cnt = 0; 
		String[] sub = subStrArr(cc(S1) + cc(S2)); // This here produces an array {a, a, aa, null, null, null} - fix that.
		
		for(int i=0; i<sub.length; i++)
			if(isPal(sub[i]))
				cnt++; 
		
		return cnt; 
	}
	
	public static void main(String[] a) {
		String[] S1 = {"a", "a", ""}; 
		String[] S2 = {"a"}; 
		
		System.out.println(count(S1, S2));
	}	
}
