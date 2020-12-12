public class Solution {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public int trap(final int[] A) {
        int l=0,r=A.length-1,l_max=0,r_max=0,res=0;
        while (l<=r) {
            if (l_max <= r_max) {
                res+=Math.max(0,l_max-A[l]);
                l_max=Math.max(l_max,A[l]);
                l++;
            } else {
                res+=Math.max(0,r_max-A[r]);
                r_max=Math.max(r_max,A[r]);
                r--;
            }
        }
        return res;
    }
}
