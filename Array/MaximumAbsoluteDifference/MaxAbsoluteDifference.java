public class Solution {
    public int maxArr(int[] A) {
        int n = A.length;
        if (n == 1){
            return 0;
        }
        int minAdd=A[0],maxAdd=A[0],minSub=A[0],maxSub=A[0];
        for(int i=0;i<n;i++){
            minAdd = Math.min(minAdd,A[i]+i);
            maxAdd = Math.max(maxAdd,A[i]+i);
            minSub = Math.min(minSub,A[i]-i);
            maxSub = Math.max(maxSub,A[i]-i);
        }
        return Math.max(maxAdd-minAdd,maxSub-minSub);
    }
}
