import java.util.Collections;
import java.util.LinkedList;


public class EllysSubstringSorter {
	
	String rearrange(String S, int idx, int L) {
		char[] c = S.toCharArray(); 
		char t; 

		// brute force sort
		for(int i=idx; i<idx+L; i++) {
			for(int j=idx; j<idx+L; j++) {
				if (c[i] < c[j]) {
					t = c[i]; 
					c[i] = c[j]; 
					c[j] = t; 
				}
			}
		}
		
//		System.out.println(S + " " + idx + " " + L + " " + new String(c)); 
		return new String(c); 
	}
	
	public String getMin(String S, int L) {
		String newS; 
		LinkedList<String> ll = new LinkedList<String>(); 
		
		for(int i=0; i<S.length()-L; i++) {
			newS = rearrange(S, i, L);  			
			System.out.println(newS); 			
			ll.add(newS); 
		}
		
		Collections.sort(ll);
		
		return ll.getFirst(); 
	}
	
	public static void main(String[] args) {
		EllysSubstringSorter ess = new EllysSubstringSorter(); 		
//		System.out.println(ess.getMin("TOPCODER", 4)); 
//		System.out.println(ess.getMin("AAAAAAAAA", 2)); 
//		System.out.println(ess.getMin("ESPRIT", 3)); 
//		System.out.println(ess.getMin("ABRACADABRA", 5)); 
//		System.out.println(ess.getMin("BAZINGA", 6)); 
//		System.out.println(ess.getMin("AAAWDIUAOIWDESBEAIWODJAWDBPOAWDUISAWDOOPAWD", 21)); 
	}
}
