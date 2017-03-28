/* 7 Reverse an Integer */

public class 7e-ReverseInteger {
    public int reverse(int x) {
        int res=0, tmp=0;
        while(x!=0) {
            tmp = tmp*10 + x%10;

            /* overflow check */
            if(tmp/10 != res)    return 0;

            res = tmp;

            x = x/10;
        }
        return res;
    }

    public static void main(String[] args) {
        7e-ReverseInteger s = new 7e-ReverseInteger();
        System.out.println(s.reverse(-1345));
    }
}

