import java.util.*;

public class Solution {
    public boolean isValid(String s) {
        if(s==null) return false;
        
        Stack<Character> st = new Stack<>();
        int len = s.length();
        
        if(len%2==1)    return false;
        
        for(int i=0; i<len; i++) {
            char c = s.charAt(i);
            
            // open brace, push to Stack
            if(c=='(' || c=='{' || c=='[') {
                st.push(c);
            } else {
                if(st.size()==0)    return false;
                
                char d = st.pop();
                if(c==')' && d!='(')    return false;
                if(c=='}' && d!='{')    return false;
                if(c==']' && d!='[')    return false;
            }
        }
        
        if(st.size()>0) return false;
        
        return true;
    }
}
