/**
 * @input A : Integer array
 * 
 * @Output Integer
 */

 func min(a int, b int) (int) {
    if a < b {
        return a
    } else {
        return b
    }
}
func max(a int, b int) (int) {
    if a > b {
        return a
    } else {
        return b
    }
}
func solve(A []int )  (int) {
    r_min := make([]int,len(A))
    r_min[len(A)-1] = A[len(A)-1]
    for i:=len(A)-2;i>=0;i-- {
        r_min[i]=min(r_min[i+1],A[i+1])
    }
    l_max := A[0]
    res := 0
    for i:=0;i<len(A);i++ {
        l_max=max(l_max,A[i])
        if i == len(A)-1 || l_max <= r_min[i] {
            res++
        }
    }
    return res
}