/* This  solution is fromm Discussion forum.  Though I provided similar
 * solution, mine was stuck in infinite loop and I looked at this
 */

public class Solution {
  
    public boolean exist(char[][] board, int row, int col, String word) {
        if(word==null || word.isEmpty())  return true;
        
        // crossed boundary
        if(row<0 || row>=board.length)  return false;
        if(col<0 || col>=board[0].length)   return false;
        
        //mismatch
        if(board[row][col] != word.charAt(0))   return false;
        
        board[row][col] = '#';
        
        //there's a match spawn calls in 4 directions
        boolean result = exist(board, row+1, col, word.substring(1, word.length())) || 
                        exist(board, row-1, col, word.substring(1, word.length())) || 
                        exist(board, row, col+1, word.substring(1, word.length())) || 
                        exist(board, row, col-1, word.substring(1, word.length()));
        
        board[row][col] = word.charAt(0);
        
        return result;
    }

    public boolean exist(char[][] board, String word) {
        // start from 1st char match
        for(int i=0; i<board.length; i++) {
            for(int j=0; j<board[0].length; j++) {
                if(exist(board, i, j, word))    return true;
            }
        }

        return false;
    }
    
    public static void main(String[] args) {
        Solution S = new Solution();
        char[][] board = {
                          {'A','B','C','E'},
                          {'S','F','C','S'},
                          {'A','D','E','E'}
                        };
        String word = "ABCCED";
        
        System.out.println(S.exist(board, word));
    }
}
