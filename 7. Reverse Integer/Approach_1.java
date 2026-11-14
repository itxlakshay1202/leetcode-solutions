class Solution {
    public int reverse(int x) {
        int soln = 0;
        if(x > 0){
        while (x > 0){
            if(soln > 214748364.7){
                return 0;
            }
            soln = soln*10 + x%10;
            System.out.println(soln);
            x /= 10;
        }
        }else{
            x = -x;
            while (x > 0){
                if(soln > 214748364.8){
                    return 0;
                }
            soln = soln*10 + x%10;
            x /= 10;
            }
            soln = -soln;
        }
            return soln;
    }
}