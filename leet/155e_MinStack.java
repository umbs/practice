import java.util.*;

public class MinStack {

    Stack<Integer> st;
    Stack<Integer> minStack;
    int min;
    
    /** initialize your data structure here. */
    public MinStack() {
        st = new Stack<>();
        minStack = new Stack<>();
        min = Integer.MAX_VALUE;
    }
    
    public void push(int x) {
        // first element
        if(st.size()==0)    min = x;
        // min element so far
        else if(x < min)    min = x;
        
        st.push(x);
        minStack.push(min);
    }
    
    public void pop() {
        if(st.size()==0)    return;
        
        st.pop();
        minStack.pop();
        
        if(st.size() != 0)  min = minStack.peek();
    }
    
    public int top() {
        if(st.size()==0)    return -1; // not sure; error condition
        return st.peek();
    }
    
    public int getMin() {
        if(minStack.size()==0)    return -1; // not sure what to do; error condition
        return minStack.peek();
    }
}
