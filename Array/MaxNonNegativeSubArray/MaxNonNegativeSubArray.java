public class Solution {
    public ArrayList<Integer> maxset(ArrayList<Integer> A) {
    int l = 0,r = 0;
    long res = -1;
    int temp_l = -1,temp_r = -1;
    long temp_sum = -1;
    for (int i=0;i<A.size();i++) {
        int val = A.get(i);
        if (val < 0 || temp_sum < 0) {
            temp_sum=val;
            temp_l = i;
            temp_r = i;
        } else {
            temp_sum+=val;
            temp_r+=1;
        }
        if ((temp_sum > res) || (temp_sum == res && (temp_r-temp_l>r-l))){
            l = temp_l;
            r = temp_r;
            res = temp_sum;
        }
    }
    ArrayList<Integer> result = new ArrayList<Integer>();
    if (res < 0){
        return result;
    }
    for(int i=l;i<=r;i++){
        result.add(A.get(i));
    }
    return result;
    }
}
