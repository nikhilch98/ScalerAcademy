vector<int> Solution::plusOne(vector<int> &A) {
    int carry = 1,least_sig_index = A.size()-1;
    vector<int> res; 
    for(int i=A.size()-1;i>=0;i--){
        int temp = A[i];
        A[i] = (temp+carry)%10;
        carry= (temp+carry)/10;
        if (A[i] != 0){
            least_sig_index = i;
        }
    }
    if (carry == 1) {
        res.push_back(1);
        least_sig_index = 0;
    }
    for(;least_sig_index<A.size();least_sig_index++){
        res.push_back(A[least_sig_index]);
    }
    return res;
}