public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Map<String, Integer> hash = new HashMap<String, Integer>();
        List<String> res = new ArrayList<>();
        
        // build hashmap
        for(int i=0; i+10<=s.length(); i++) {
            String sub = s.substring(i, i+10);
            hash.put(sub, hash.getOrDefault(sub, 0)+1);
        }
        
        // get strings with at least 2 occurances
        for(String key : hash.keySet()) {
            Integer cnt = hash.get(key);
            if(cnt != null && cnt.intValue()>1) res.add(key);
        }
        
        return res;
    }
}
