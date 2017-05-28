public class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> ll = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList();
        
        if(root==null)  return ll;
        
        q.add(root);
        
        while(!q.isEmpty()) {
            int level = q.size();
            List<Integer> l = new LinkedList<>();
            
            /* Add all children of one level to 'l' */
            for(int i=0; i<level; i++) {
                if(q.peek().left != null)   q.add(q.peek().left);
                if(q.peek().right != null)  q.add(q.peek().right);
                l.add(q.poll().val);
            }
            
            ll.add(l);
        }
        
        int i=0, j=ll.size()-1;

        for(; i<j; i++, j--) {
            List<Integer> m = ll.get(i);
            List<Integer> n = ll.get(j);
            
            ll.set(i, n); 
            ll.set(j, m);
        }
        
        return ll;       
    }
}
