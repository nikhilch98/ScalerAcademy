int Solution::maxArr(vector<int> &A) {
    int n = A.size();
    if (n == 1){
        return 0;
    }
    int minAdd=A[0],maxAdd=A[0],minSub=A[0],maxSub=A[0];
    for(int i=0;i<n;i++){
        minAdd = min(minAdd,A[i]+i);
        maxAdd = max(maxAdd,A[i]+i);
        minSub = min(minSub,A[i]-i);
        maxSub = max(maxSub,A[i]-i);
    }
    return max(maxAdd-minAdd,maxSub-minSub);
}