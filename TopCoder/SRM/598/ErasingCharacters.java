import java.util.*;
import java.util.regex.*;
import java.text.*;
import java.math.*;


public class ErasingCharacters
{
	public String simulate(String s)
	{
		StringBuilder newStr = new StringBuilder(s); 
		
		for(int i=0; i < newStr.length(); ) {
			// last char of string
			if(i+1 == newStr.length()) 
				return newStr.toString(); 
			
			// neighbor match
			if(newStr.charAt(i) == newStr.charAt(i+1)) {
				// delete match and create new stringBuilder
				newStr = newStr.delete(i, i+2); 
				// reset counter
				i = 0; 
				continue; 
			}
			
			i++; 
		}
		
		return newStr.toString(); 
	}
}
//Powered by KawigiEdit 2.1.4 (beta) modified by pivanof!