/**
 * @input A : Integer array
 * 
 * @Output Integer
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
func trap(A []int )  (int) {
    l_max,r_max,l,r,res:=0,0,0,len(A)-1,0
    for (l<=r) {
        if l_max <= r_max {
            res+=max(0,l_max-A[l])
            l_max = max(l_max,A[l])
            l+=1
        } else {
            res+=max(0,r_max-A[r])
            r_max = max(r_max,A[r])
            r-=1
        }
    }
    return res
}
