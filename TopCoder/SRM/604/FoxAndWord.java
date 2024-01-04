import java.util.Arrays;


public class FoxAndWord {

	public int howManyPairs(String[] w) {
		int res = 0; 
		String comb; 
		int[] sanity = new int[w.length]; 
				
		for(int i=0; i<w.length; i++) {
			Arrays.fill(sanity, 0);
			
			for(int j=1; j<w[i].length(); j++) {
				comb = w[i].substring(j)+w[i].substring(0, j);
				
				for(int k=i+1; k<w.length; k++)
					if(w[k].equals(comb) && sanity[k] != 1) {
						sanity[k] = 1; 
						res++;
					}
			}
		}
		return res; 
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		FoxAndWord fw = new FoxAndWord(); 
		String s1[] = {"tokyo", "kyoto"}; 
		String s2[] = {"aaaaa", "bbbbb"}; 
		String s3[] = {"ababab","bababa","aaabbb"}; 
		String s4[] = {"eel", "ele", "lee"}; 
		String s5[] = {"aaa", "aab", "aba", "abb", "baa", "bab", "bba", "bbb"}; 
		String s6[] = {"top","coder"}; 
		
		System.out.println(fw.howManyPairs(s1)); 
		System.out.println(fw.howManyPairs(s2)); 
		System.out.println(fw.howManyPairs(s3)); 
		System.out.println(fw.howManyPairs(s4)); 
		System.out.println(fw.howManyPairs(s5)); 
		System.out.println(fw.howManyPairs(s6)); 
	}
}
