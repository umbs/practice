import java.util.Stack;


public class DFS {

	class Node {
		boolean visited; 
		int val; 
		
		Node(int val) {
			this.val = val; 
		}
	}
	
	public void dfsWalk(Node root) 
	{
		Stack<Node> s = new Stack<Node>();
		Node n; 
		
		root.visited = false; 
		
		s.push(root); 
		
		while(!s.empty()) {
			n = s.pop();
			n.visited = true; 
			
			/* do operation */
			/* for each unvisited neighbor, push it to s */ 
		}
	}
}
