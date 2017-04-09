/* 535m - Encode and Decode TinyURL
 */
import java.util.*;

public class Solution {
    public Hashtable<String, String> ht = new Hashtable<String, String>();
    public Random r = new Random();

    public String encode(String longUrl) {
        int key = r.nextInt();
        if(key<0) key = -key; // only positive ints
        String keyString = Integer.toString(key);

        ht.put(keyString, longUrl);

        return keyString;
    }

    public String decode(String shortUrl) {
        Object longUrl = ht.get(shortUrl);

        if(longUrl == null) return "";
        return (String) longUrl;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String enc = s.encode("Hello");
        System.out.println("Decode: " + s.decode(enc));
    }
}
