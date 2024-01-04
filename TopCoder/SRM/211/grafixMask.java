import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;


public class grafixMask {
	class Node {
		int x, y; 
		
		Node(int x, int y) {
			this.x = x; 
			this.y = y;
		}
	}

	int width = 400, height = 600; 
	boolean pix[][] = new boolean[width][height];
	
	private boolean isOpen(int x, int y) {
		if (x<0 || x>=width)
			return false; 
		else if (y<0 || y>=height)
			return false; 
		else if (pix[x][y] == false)
			return false; 
		else 
			return true; 
	}
	
	public int[] sortedAreas(String[] rect) {
		ArrayList<Integer> noAreas = new ArrayList<Integer>(); 
		Node n; 
		Stack<Node> s = new Stack<Node>(); 
		int areas; 
		
		for(boolean[] row: pix)
			Arrays.fill(row, true);
		
		// mark all opaque regions
		for(int i=0; i<rect.length; i++) {
			int x1, x2, y1, y2; 
			StringTokenizer st = new StringTokenizer(rect[i]); 
			
			x1 = Integer.parseInt(st.nextToken()); 
			y1 = Integer.parseInt(st.nextToken()); 
			x2 = Integer.parseInt(st.nextToken()); 
			y2 = Integer.parseInt(st.nextToken()); 
			
			// all opaque regions 
			for(int k=x1; k<=x2; k++)
				for(int j=y1; j<=y2; j++)
					pix[k][j] = false; 
		}
		
		for(int i=0; i<width; i++) {
			for(int j=0; j<height; j++) {
				if(pix[i][j] == false)
					continue; 
								
				s.push(new Node(i,j));
				areas = 0; 
				
				while(s.size() > 0) {
					n = s.pop(); 
					pix[n.x][n.y] = false; //visited 
					areas++; 
					
					// left
					if(isOpen(n.x-1, n.y)) 
						s.push(new Node(n.x-1, n.y)); 
					
					// right
					if(isOpen(n.x+1, n.y)) 
						s.push(new Node(n.x+1, n.y)); 

					// bottom
					if(isOpen(n.x, n.y-1)) 
						s.push(new Node(n.x, n.y-1)); 
					
					// top
					if(isOpen(n.x, n.y+1)) 
						s.push(new Node(n.x, n.y+1)); 					
				}
				
				System.out.println("SA: " + areas); 
				noAreas.add(areas); 
			}
		}
		
		int[] totalAreas = new int[noAreas.size()]; 
		
		for(int i=0; i<noAreas.size(); i++)
			totalAreas[i] = ((Integer) noAreas.get(i)).intValue(); 

		Arrays.sort(totalAreas); 
		return totalAreas; 
	}
	
	public static void main(String[] args) {
		grafixMask gm = new grafixMask();
//		String[] s = {"4 0 6 9"}; 
//		String[] s = {"0 292 399 307"}; 
		String[] s = {"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}; 
		
		int[] areas = gm.sortedAreas(s);
		
		for(int i=0; i<areas.length; i++)
			System.out.println(areas[i] + " ");
	}
}