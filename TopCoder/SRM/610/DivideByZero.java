import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;


public class DivideByZero {

	public int CountNumbers(int[] arr) {
		LinkedList ll = new LinkedList();
		int[] num = arr; 
		int res=0; 

		if(arr.length == 1)
			return 1; 
		
		// sort array
		Arrays.sort(num);
		
		while (true) {
			
			for(int i=num.length-1; i>=0; --i) {
				for(int j=i-1; j>=0; --j) {
					if(!ll.contains(num[i]))
						ll.add(num[i]); 
	
					if(!ll.contains(num[j]))
						ll.add(num[j]); 
	
					int div = num[i]/num[j];
//					System.out.println(div); 
					
					if(!ll.contains(div))
						ll.add(div); 
				}
			}
			
			if(num.length == ll.size()) {
				res = ll.size(); 
				break; 
			}
			else {
				num = new int[ll.size()]; 
				
				for(int i=0; i<num.length; i++)
					num[i] = (Integer) ll.get(i); 
				
				Arrays.sort(num);
			}
			
		}
				
		return res; 
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DivideByZero dz = new DivideByZero();
//		int[] n = {9, 2}; 
//		int[] n = {8, 2}; 
//		int[] n = {50}; 
//		int[] n = {1, 5, 8, 30, 15, 4};
//		int[] n = {1, 2, 4, 8, 16, 32, 64}; 
		int[] n = {6, 2, 18}; 
		
		System.out.println(dz.CountNumbers(n)); 
	}

}
