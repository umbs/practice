import java.util.LinkedList;


public class BFS {
	class Node {
		boolean visited; 
		int val; 
		
		Node(int val) {
			this.val = val; 
		}
	}
	
	public void bfsWalk(Node root) {
		LinkedList<Node> que = new LinkedList<BFS.Node>(); 
		Node n; 
		
		root.visited = false; 		
		que.addLast(root);
		
		while(que.size() != 0) {
			n = que.removeFirst(); 
			n.visited = true; 
			
			/* do operation on n */
			/* add each unvisited neighbor of n to que */
		}
	}
}
