/* 
Time Complexity  : O(n)
Space Complexity : O(1)
*/
int Solution::maxSubArray(const vector<int> &A) {
    int res = A[0],temp=A[0];
    for(int i=1;i<A.size();i++){
        temp = max(A[i],temp+A[i]);
        res = max(res,temp);
    }
    return res;
}
