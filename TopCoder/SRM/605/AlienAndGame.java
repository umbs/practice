
public class AlienAndGame {

	boolean opp(int a, int b) {
		return (a<0 && b>0) || (a>0 && b<0); 
	}
	
	public int getNumber(String[] b) {
		int h, w; 
		h = b.length; 
		w = b[0].length(); 
		
		int acc[][] = new int[h][w]; 
		
		// compute width and heights 
		for(int i=0; i<h; i++) {
			for(int j=0; j<w; j++) {
				if(b[i].charAt(j) == 'A') {
					acc[i][j] = 1; 
					if(j>0 && b[i].charAt(j-1) == 'A')
						acc[i][j] += acc[i][j-1]; 
				}
				else {
					acc[i][j] = -1; 
					if(j>0 && b[i].charAt(j-1) == 'B')
						acc[i][j] += acc[i][j-1]; 
				}
			}
	 	}
		
		int area = 0; 
		
		for(int i=0; i<h; i++) {
			for(int j=0; j<w; j++) {
				int side = acc[i][j]; 
				area = Math.max(area, side * side); 

				for (int k=i+1; k<h; k++) {
					// next row is opp color & within length 'side'
					if(Math.abs(acc[k][j])<acc[i][j])
						break; 
					
				}
			}
		}
	
		return area; 
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
