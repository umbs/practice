import java.util.LinkedList;


public class AlienAndPassword {

	public int getNumber(String s) {
		LinkedList ll = new LinkedList(); 
		String n;  
		int count=0; 
		
		if (s.length() == 1)
			return 1; 
		
		ll.add(s.substring(1)); 
		count++; 
		
		for(int i=1; i<s.length(); i++) {
			n = s.substring(0,i) + s.substring(i+1); 
			if(!ll.contains(n)) {
				count++; 
				ll.add(n); 
			}
		}
		
		return count; 
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AlienAndPassword ap = new AlienAndPassword(); 
		String s1 = "A"; 
		String s2 = "ABA"; 
		String s3 = "AABACCCCABAA"; 
		String s4 = "AGAAGAHHHHFTQLLAPUURQQRRRUFJJSBSZVJZZZ"; 
		String s5 = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"; 

		System.out.println(ap.getNumber(s1)); 
		System.out.println(ap.getNumber(s2)); 
		System.out.println(ap.getNumber(s3)); 
		System.out.println(ap.getNumber(s4)); 
		System.out.println(ap.getNumber(s5)); 

	}

}
