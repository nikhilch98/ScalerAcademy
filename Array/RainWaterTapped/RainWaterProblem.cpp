int Solution::trap(const vector<int> &A) {
    int l=0,r=A.size()-1,l_max=0,r_max=0,res=0;
    while (l<=r) {
        if (l_max <= r_max) {
            res+=max(0,l_max-A[l]);
            l_max=max(l_max,A[l]);
            l++;
        }
        else {
            res+=max(0,r_max-A[r]);
            r_max=max(r_max,A[r]);
            r--;
        }
    }
    return res;
}
