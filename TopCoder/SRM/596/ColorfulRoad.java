import java.util.Arrays;

public class ColorfulRoad {
	
	static boolean isValidChar(char a, char b) {
		if (a=='R' && b=='G') return true; 
		if (a=='G' && b=='B') return true; 
		if (a=='B' &&b=='R') return true;
		
		return false; 
	}
	
	static int getMin(String road) {
		int energy[] = new int[15];
		int temp; 
		Arrays.fill(energy, 225);
		
		energy[0] = 0; 
		for(int i=1; i<road.length(); i++) {
			for(int j=0; j<i; j++) {
				if(isValidChar(road.charAt(j), road.charAt(i))) {
					temp = energy[j] + (i-j)*(i-j); 
					
					if(energy[i] > temp)
						energy[i] = temp; 
				}
			}
		}
		
		temp = energy[road.length()-1]; 
		
		return (temp == 225 ? -1 : temp)  ; 
	}
	
	public static void main(String[] args) {
		System.out.println(getMin("RBBGGGRR")); 
	}
}
