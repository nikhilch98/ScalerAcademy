/**
 * @input A : Integer array
 * 
 * @Output Integer

 Time Complexity  : O(n)
 Space Complexity : O(1)
 */
func min(a int, b int) (int) {
    if a < b {
        return a
    }
    return b
}
func max(a int, b int) (int) {
    if a > b {
        return a
    }
    return b
}
func maxSubArray(A []int )  (int) {
    res,temp:=A[0],A[0]
    for _,val:=range A[1:]{
        temp=max(val,val+temp)
        res=max(res,temp)
    }
    return res
}
