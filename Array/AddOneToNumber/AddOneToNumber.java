public class Solution {
    public ArrayList<Integer> plusOne(ArrayList<Integer> A) {
        
        int carry = 1,least_significant_index = A.size()-1;
        ArrayList<Integer> res = new ArrayList<Integer>();
        for(int i=A.size()-1;i>=0;i--){
            int temp = A.get(i);
            A.set(i,(temp+carry)%10);
            carry = (temp+carry)/10;
            if(A.get(i) != 0) {
                least_significant_index = i;
            }
        }
        if( carry == 1){
            res.add(carry);
            least_significant_index = 0;
        }
        for(;least_significant_index<A.size();least_significant_index++){
            res.add(A.get(least_significant_index));
        }
        return res;
    }
}