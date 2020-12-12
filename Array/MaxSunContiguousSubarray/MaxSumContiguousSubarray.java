public class Solution {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    // Time Complexity  : O(n)
    // Space Complexity : O(1)
    public int maxSubArray(final int[] A) {
        int res=A[0],temp=A[0];
        for(int i=1;i<A.length;i++){
            temp=Math.max(A[i],temp+A[i]);
            res=Math.max(res,temp);
        }
        return res;
    }
}
