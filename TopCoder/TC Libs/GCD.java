
public class GCD {
	
	public int gcdEuclid(int a, int b) {
		if(b==0) return a; 
		return gcdEuclid(b, a%b); 
	}

	public int gcd(int a, int b) {
		while(a != b) {
			if (a>b)  a -= b; 
			else      b -= a; 
		}
		
		return a; 
	}

	public int binaryGCD(int a, int b) {
		if(a==0) return b; 
		if(b==0) return a; 
		
		int res=0; 
		
		if(a%2 == 0 && b%2 == 0)
			res = 2 * binaryGCD(a/2, b/2); 
		
		else if(a%2 == 0 && b%2 != 0)
			res = binaryGCD(a/2, b); 
		
		else if(a%2 != 0 && b%2 == 0)
			res = binaryGCD(a, b/2);
		else {
			if(a>b) res = binaryGCD((a-b)/2, b); 
			else res = binaryGCD((b-a)/2, b); 
		}
		
		return res; 
	}
}
