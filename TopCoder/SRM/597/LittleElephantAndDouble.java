import java.util.*;
import java.util.regex.*;
import java.text.*;
import java.math.*;


public class LittleElephantAndDouble
{
    private String result = "YES"; 
    
	public String getAnswer(int[] A)
	{
		int max = 0, maxIndex = 0; 
		for (int i=0; i < A.length; i++) {
			if(A[i] > max) {
				max = A[i]; 
				maxIndex = i; 
			}
		}
		
		for(int i=0; i < A.length; i++) {
			int x = A[i]; 
			
			if(i == maxIndex)
				continue; 
			
			while (x<max) 
				x = x*2; 
			
			if(x > max) {
				result = "NO"; 
				break; 
			}
		}
	    	return result; 
	}
}
