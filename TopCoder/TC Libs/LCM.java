
public class LCM {
	public int gcd(int a, int b) {
		while(a != b) {
			if (a>b)  a -= b; 
			else      b -= a; 
		}
		
		return a; 	
	}
	
	/* Using GCD */
	public int lcmGcd(int a, int b) {
		int g = gcd (a, b); 
		
		return (a/g) *b; 
	}
	
	/* without using GCD */
	public int lcmNoGcd(int a, int b) {
		int m=a, n=b; 
		
		while(a!=b)
			if (a<b) a += m; 
			else  	 b += n; 
		
		return a; 
	}
}
