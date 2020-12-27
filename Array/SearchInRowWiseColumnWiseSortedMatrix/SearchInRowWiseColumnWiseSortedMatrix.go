/**
 * @input A : 2D integer array 
 * @input B : Integer
 * 
 * @Output Integer
 */
 func solve(A [][]int , B int )  (int) {
    rows,cols:=len(A),len(A[0])
    i,j := 0,cols-1
    for (i<rows && j >=0) {
        if A[i][j]==B {
            return ((i+1)*1009+j+1)
        } else if A[i][j]>B {
            j--
        } else {
            i++
        }
    }
    return -1
}
