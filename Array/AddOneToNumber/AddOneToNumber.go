/**
 * @input A : Integer array
 * 
 * @Output Integer array.
 */
 func plusOne(A []int )  ([]int) {
    carry := 1
    least_sig_index := len(A)-1
    res := []int{}
    for i:=len(A)-1;i>=0;i--{
        A[i],carry=(A[i]+carry)%10,(A[i]+carry)/10
        if A[i] != 0{
            least_sig_index = i
        }
    }
    if carry == 1 {
        res = append(res,1)
        least_sig_index = 0
    }
    res = append(res,A[least_sig_index:]...)
    return res
}