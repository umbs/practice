/* Not my solution */
public class EllysNumberGuessing {
	
	int getNumber(int[] guesses, int[] answers)
	{
	    // find the two candidates:
	    int options[] = { guesses[0] + answers[0], guesses[0] - answers[0] };
	    int res = -2;
	    // for each candidate:
	    for (int x: options) {
	        // must be within bounds
	        boolean valid = (1 <= x && x <= 1000000000);
	        
	        if(!valid)
	        	continue; 
	        
	        // must obey all the conditions
	        for (int i = 0; i < guesses.length; i++) {
	            valid = valid && (Math.abs(guesses[i] - x) == answers[i] );
	        }
	        
	        if (valid) {
	            if (res != -2) {
	                res = -1;    // found a previous answer, set result to -1
	            } else {
	                res = x;    // save answer
	            }
	        }
	    }
	    return res;
	}
	
	public static void main(String[] args) 
	{
		EllysNumberGuessing eng = new EllysNumberGuessing(); 
		
//		int[] g = {600, 594}; 
//		int[] ans = {6, 12}; 
//		int[] g = {100, 50, 34, 40}; 
//		int[] ans = {58, 8, 8, 2}; 	
		
//		int[] g = {500000, 600000, 700000}; 
//		int[] ans = {120013, 220013, 79987}; 
		
		int[] g = {76938260, 523164588, 14196746, 296286419, 535893832,
			 41243148, 364561227, 270003278, 472017422, 367932361,
			 395758413, 301278456, 186276934, 316343129, 336557549,
			 52536121, 98343562, 356769915, 89249181, 335191879}; 

		int[] ans =	{466274085, 20047757, 529015599, 246925926, 7318513,
			 501969197, 178651118, 273209067, 71194923, 175279984,
			 147453932, 241933889, 356935411, 226869216, 206654796,
			 490676224, 444868783, 186442430, 453963164, 208020466}; 
		
		System.out.println(eng.getNumber(g, ans)); 
	}
}