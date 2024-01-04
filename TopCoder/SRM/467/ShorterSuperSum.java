
public class ShorterSuperSum {
	static int totalSum; 
//	static int matrix[][] = new int[15][15];
	
	static int calculate(int k, int n) {
		if (k==0) {
			//System.out.println(k + " " + n + " = " + n); 
			totalSum += n;
//			matrix[k][n] = n; 
			return n; 
		}
		
//		if (matrix[k][n] != 0) {
//			System.out.println("Exists (" + k + "," + n + ") - " + matrix[k][n]); 
//			totalSum += matrix[k][n]; 
//			return matrix[k][n]; 
//		}
		
//		System.out.println("Find: " + k + " " + n); 
		for(int i=1; i<=n; i++) {
			calculate(k-1, i);
//			 matrix[k-1][i] = calculate(k-1, i);
//			 totalSum += calculate(k-1, i);  this is incorrect, investigate why. 
		}
		
		return totalSum; 
	}
	
	public static void main(String[] args) {
		System.out.println(calculate(4, 10));
	}
}
