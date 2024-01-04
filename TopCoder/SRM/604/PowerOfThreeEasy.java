import java.util.LinkedList;

/* This code fails system test on 9999999, 9999999 test case due to timing. Fix the break condition 
 */
public class PowerOfThreeEasy {

	class coord { 
		int x; int y;
		coord(int x, int y) {
			this.x = x; this.y = y; 
		}
	}
	
	int pow3[] = new int[19]; // 3^19 < 2^31 (largest int) 
	
	void power3(int max) {
		pow3[0] = 1; 
		
		for(int k=1; k<19; k++) 
			if (pow3[k] < max)
				pow3[k] = pow3[k-1]*3; 
		
	}
	
	public String ableToGet(int x, int y) {
		LinkedList<coord> ll = new LinkedList<PowerOfThreeEasy.coord>(); 
		int step = 0, a, b, jump; 
		String res = "Impossible"; 

		power3(Math.max(x, y)); 
		
		coord c = new coord(0, 0); 
		ll.add(c); 
				
		coord temp, marker;
		marker = new coord(-1, -1); 
		ll.add(marker); //level marker
		
		// BFS
		while(ll.size() > 0) {
			temp = ll.removeFirst(); 
			
			if (temp.x == x && temp.y == y) {
				res = "Possible"; 
				break; 
			}
			
			jump = pow3[step]; 
			
			if (temp.x > x && temp.y > y) {
				res = "Impossible"; 
				break;
			}
			
			// end of level 
			if (temp.x == -1 && temp.y == -1) {
				ll.add(marker); // end marker end of queue 
				step++; 
				continue; 
			}
			
			a = temp.x + jump; // left branch 
			b = temp.y + jump; // right branch 
			
			ll.add(new coord(a, temp.y)); 
			ll.add(new coord(temp.x, b)); 
		}
		
		return res; 
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PowerOfThreeEasy p = new PowerOfThreeEasy(); 
		
		System.out.println(p.ableToGet(1, 3)); 
		System.out.println(p.ableToGet(1, 1)); 
		System.out.println(p.ableToGet(3, 0)); 
		System.out.println(p.ableToGet(1, 9)); 
		System.out.println(p.ableToGet(3, 10)); 
		System.out.println(p.ableToGet(1093, 2187)); 
		System.out.println(p.ableToGet(0, 0)); 

	}

}
