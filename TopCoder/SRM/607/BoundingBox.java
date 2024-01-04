import java.util.Arrays;


public class BoundingBox {
	public int smallestArea(int[]x, int[]y) {
		Arrays.sort(x);
		Arrays.sort(y);
		
		int len = x[x.length-1] - x[0]; 
		int hi  = y[y.length-1] - y[0]; 
		
		return Math.abs(len * hi); 
	}	
}
