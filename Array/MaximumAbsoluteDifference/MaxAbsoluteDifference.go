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
func maxArr(A []int ) (int) {
    if len(A) == 1{
        return 0
    }
    minAdd,maxAdd,minSub,maxSub:=A[0],A[0],A[0],A[0]
    for i,val := range A{
        minAdd = min(minAdd,val+i)
        maxAdd = max(maxAdd,val+i)
        minSub = min(minSub,val-i)
        maxSub = max(maxSub,val-i) 
    }
    return max(maxAdd-minAdd,maxSub-minSub)
}
