public class InterestingNumber {

	public String isInteresting(String x) {
		int len = x.length(); 
		int[] n = new int[len]; 
		int[] c = new int[len]; 
		
		String res = "Interesting"; 
		
		for(int i=0; i<len; i++) {
			n[i] = x.charAt(i)-'0';
			c[i] = 0; 
			
//			System.out.print(n[i] + " "); 
		}
		
		for(int l=0; l<len; l++) {
			
			// already visited, move on
			if(n[l] == -1) 
				continue; 
			
			int gap = n[l]+1; 
			
			// next number is out of bounds 
			if(l+gap >= x.length()) {
				res = "Not interesting"; 
				break; 
			}
			
			if(n[l] != n[l+gap]) {
				res = "Not interesting"; 
				break; 
			}
			
			// two times
			if(c[n[l]] == 2) {
				res = "Not interesting"; 
				break;
			}
			
			// probably interesting
			if(n[l] == n[l+gap]) {
				c[n[l]] = 2; 
				n[l] = n[l+gap] = -1; 
				continue; 
			}				
		}
		
		return res; 
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		InterestingNumber in = new InterestingNumber();

		System.out.println(in.isInteresting("2002")); 
		System.out.println(in.isInteresting("1001")); 
		System.out.println(in.isInteresting("41312432")); 
		System.out.println(in.isInteresting("611")); 
		System.out.println(in.isInteresting("64200246")); 
		System.out.println(in.isInteresting("631413164")); 
		System.out.println(in.isInteresting("200200")); 

	}

}
