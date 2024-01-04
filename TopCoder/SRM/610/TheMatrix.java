// Based on solution from 'chokudai' 

public class TheMatrix {

	public int MaxArea(String[] b) {
		int i, j, k, h, w, res = 0;
		
		h = b.length; 
		w = b[0].length(); 
		
		int[][]count = new int[h][w]; 
		
		// measure lengths 
		for(i=0; i<h; i++) {
			for(j=0; j<w; j++) {
				count[i][j] = 1;
				
				if(j>0 && b[i].charAt(j) != b[i].charAt(j-1))
					count[i][j] = count[i][j-1]+1; 
			}
		}
		
		for(i=0; i<h; i++) {
			for(j=0; j<w; j++) {
				res = Math.max(res, count[i][j]); 
				int len = count[i][j]; 
				
				for(k=i+1; k<h; k++) {
					// no longer a chess board
					if(b[k].charAt(j) == b[k-1].charAt(j))
						break; 
					
					// max len of rect so far 
					len = Math.min(len,  count[k][j]); 
					
					// area of rect 
					res = Math.max(res, len * (k-i+1)); 
				}
			}
		}
		
		return res; 
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
}
